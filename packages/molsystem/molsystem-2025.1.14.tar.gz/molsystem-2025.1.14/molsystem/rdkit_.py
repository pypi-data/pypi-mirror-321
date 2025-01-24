# -*- coding: utf-8 -*-

"""Interface to RDKit."""

import logging
import json
import pprint


try:
    from rdkit import Chem
except ModuleNotFoundError:
    print(
        "Please install rdkit using conda:\n" "     conda install -c conda-forge rdkit"
    )
    raise

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# Valence
valence = {
    1: 1,
    2: 0,
    3: 1,
    4: 2,
    5: 3,
    6: 4,
    7: 3,
    8: 2,
    9: 1,
    10: 0,
    11: 1,
    12: 2,
    13: 3,
    14: 4,
    15: 3,
    16: 2,
    17: 1,
    18: 0,
    92: 2,
}


def rdkit_version():
    """Return the RDKit version."""
    return Chem.rdBase.rdkitVersion


class RDKitMixin:
    """A mixin for handling RDKit via its Python interface."""

    def to_RDKMol(self, properties=None):
        """Return an RDKMol object for the configuration, template, or subset."""
        index = {}
        indices = []
        rdk_mol = Chem.RWMol()
        for atno, _id in zip(self.atoms.atomic_numbers, self.atoms.ids):
            atom = Chem.Atom(atno)
            idx = rdk_mol.AddAtom(atom)
            index[_id] = idx
            indices.append(idx)

        bond_types = {
            1: Chem.BondType.SINGLE,
            2: Chem.BondType.DOUBLE,
            3: Chem.BondType.TRIPLE,
            5: Chem.BondType.AROMATIC,
        }
        for row in self.bonds.bonds():
            rdk_mol.AddBond(
                index[row["i"]], index[row["j"]], bond_types[row["bondorder"]]
            )

        # Check for NH4+ type groups and set their charge
        rdk_mol.UpdatePropertyCache(strict=False)
        for at in rdk_mol.GetAtoms():
            atno = at.GetAtomicNum()
            if atno in valence:
                charge = at.GetExplicitValence() - valence[atno]
                if charge != 0 and at.GetFormalCharge() == 0:
                    at.SetFormalCharge(charge)

        natom = self.atoms.n_atoms
        conf = Chem.Conformer(natom)
        for idx, xyz in zip(indices, self.atoms.coordinates):
            conf.SetAtomPosition(idx, xyz)

        rdk_mol.AddConformer(conf)
        try:
            Chem.SanitizeMol(rdk_mol)
        except Chem.KekulizeException as e:
            logger.warning(f"Kekulization failed: {e}")
            flags = (
                Chem.SanitizeFlags.SANITIZE_ALL ^ Chem.SanitizeFlags.SANITIZE_KEKULIZE
            )
            Chem.rdmolops.SanitizeMol(rdk_mol, sanitizeOps=flags)

        # Add the net charge and spin multiplicity as properties for configurations
        if self.__class__.__name__ == "_Configuration":
            rdk_mol.SetIntProp("SEAMM|net charge|int|", self.charge)
            rdk_mol.SetIntProp("SEAMM|spin multiplicity|int|", self.spin_multiplicity)
            rdk_mol.SetProp("SEAMM|XYZ|json|", json.dumps(self.coordinates))

        if properties is not None:
            data = self.properties.get(properties, include_system_properties=True)
            for _property, value in data.items():
                _type = self.properties.type(_property)
                units = self.properties.units(_property)
                value = value["value"]
                key = f"SEAMM|{_property}|{_type}|"
                if units is not None and units != "":
                    key += units

                if _type == "int":
                    rdk_mol.SetIntProp(key, value)
                elif _type == "float":
                    rdk_mol.SetDoubleProp(key, value)
                elif _type == "json":
                    rdk_mol.SetProp(key, json.dumps(value))
                else:
                    rdk_mol.SetProp(key, str(value))

        return rdk_mol

    def from_RDKMol(
        self, rdk_mol, properties="all", atoms=True, coordinates=True, bonds=True
    ):
        """Transform an RDKit molecule into the current object.

        Parameters
        ----------
        rdk_mol : rdkit.chem.molecule
            The RDKit molecule object

        properties : str = "all"
            Whether to include all properties or none

        atoms : bool = True
            Recreate the atoms

        coordinates : bool = True
            Update the coordinates

        bonds : bool = True
            Recreate the bonds from the RDKit molecule

        Returns
        -------
        molsystem._Configuration
        """
        atnos = []
        for rdk_atom in rdk_mol.GetAtoms():
            atnos.append(rdk_atom.GetAtomicNum())
            logger.debug(f"atom {atnos}")

        # TODO: Generalize to handling multiple conformers
        # in a rdk_mol object, if necessary
        Xs = []
        Ys = []
        Zs = []
        for rdk_conf in rdk_mol.GetConformers():
            for atom_coords in rdk_conf.GetPositions():
                Xs.append(atom_coords[0])
                Ys.append(atom_coords[1])
                Zs.append(atom_coords[2])
                logger.debug(f"{atom_coords[0]} {atom_coords[1]} {atom_coords[2]}")

        Is = []
        Js = []
        BondOrders = []
        bond_types = {
            Chem.BondType.SINGLE: 1,
            Chem.BondType.DOUBLE: 2,
            Chem.BondType.TRIPLE: 3,
            Chem.BondType.AROMATIC: 5,
        }
        for rdk_bond in rdk_mol.GetBonds():
            i = rdk_bond.GetBeginAtom().GetIdx()
            j = rdk_bond.GetEndAtom().GetIdx()
            bondorder = bond_types[rdk_bond.GetBondType()]
            Is.append(i)
            Js.append(j)
            BondOrders.append(bondorder)
            logger.debug(f"bond {i} - {j} {bondorder}")

        if atoms:
            self.clear()
            ids = self.atoms.append(x=Xs, y=Ys, z=Zs, atno=atnos)
        else:
            ids = self.atoms.ids

            if coordinates:
                xyz = [[x, y, z] for x, y, z in zip(Xs, Ys, Zs)]
                self.atoms.coordinates = xyz

        if atoms or bonds:
            i = [ids[x] for x in Is]
            j = [ids[x] for x in Js]
            self.bonds.append(i=i, j=j, bondorder=BondOrders)

        data = rdk_mol.GetPropsAsDict()
        if self.__class__.__name__ == "_Configuration":
            # Charge
            self.charge = int(Chem.GetFormalCharge(rdk_mol))

            # Calculate spin multiplicity assuming maximal spin
            n_electrons = 0
            for rdk_atom in rdk_mol.GetAtoms():
                n_electrons += rdk_atom.GetNumRadicalElectrons()
            self.spin_multiplicity = n_electrons + 1

            # Check for property items for charge and multiplicity
            if "SEAMM|net charge|int|" in data:
                self.charge = int(data["SEAMM|net charge|int|"])
                del data["SEAMM|net charge|int|"]
            if "SEAMM|spin multiplicity" in data:
                self.spin_multiplicity = int(data["SEAMM|spin multiplicity|int|"])
                del data["SEAMM|spin multiplicity|int|"]

            # Coordinates
            if "SEAMM|XYZ|json|" in data:
                self.coordinates = json.loads(data["SEAMM|XYZ|json|"])
                del data["SEAMM|XYZ|json|"]

        # Record any properties in the database if desired
        if properties == "all":
            for key, value in data.items():
                if key.startswith("SEAMM|"):
                    _, _property, _type, units = key.split("|", 4)
                    units = None if units.strip() == "" else units
                    if not self.properties.exists(_property):
                        self.properties.add(_property, _type=_type, units=units)

                    if _type == "json":
                        value = json.dumps(value)

                    self.properties.put(_property, value)
                else:
                    if not self.properties.exists(key):
                        _type = value.__class__.__name__
                        self.properties.add(key, _type)

                    self.properties.put(key, value)
        return self

    def debug_print(self):
        pprint.pprint(str(self.atoms._atom_table))
        pprint.pprint(str(self.atoms._coordinates_table))
        pprint.pprint(str(self.bonds))
