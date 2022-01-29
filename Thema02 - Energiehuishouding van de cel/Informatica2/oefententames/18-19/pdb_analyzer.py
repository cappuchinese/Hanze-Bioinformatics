#!/usr/bin/env python3

import sys
import chem


# Input (with positions)
# 0         1         2         3         4         5         6         7
# 01234567890123456789012345678901234567890123456789012345678901234567890123456789
# ATOM      2  CA  ALA A   1      94.840  39.132  48.940  0.00  0.00           C
#             name res ch resnum     x      y       z       q    b             elem


AMINO = "ALA CYS ASP GLU PHE GLY HIS ILE LYS LEU MET ASN PRO GLN ARG SER THR VAL TRP TYR".split()


def atom(atomstring):
    """
    collect needed data from the atomstring
    :param atomstring:
    :return:
    """
    name = atomstring[12:16].strip()
    elem = atomstring[77:79].strip()
    residue = atomstring[17:20]
    resnum = atomstring[22:26]
    chain = atomstring[21]
    x = atomstring[30:38]
    y = atomstring[38:46]
    z = atomstring[46:54]
    q = atomstring[54:60]
    b = atomstring[60:66]
    return chain, residue, resnum, name, elem


def read_atoms(pdbfile):
    """
    read file and look for the atoms
    :param pdbfile:
    :return:
    """
    opened = open(pdbfile)
    atoms = []
    #TODO
    atoms = [atoms.append(atom(line)) for line in opened
             if line.startswith("ATOM") or line.startswith("HETATM")]
    # for line in opened:
    #     if line.startswith("ATOM") or line.startswith("HETATM"):
    #         atoms.append(atom(line))
    return atoms


def per_residue(atomlist):    
    """

    :param atomlist:
    :return:
    """
    numbers = {}
    mass = {}
    for residue in AMINO:
        numbers[residue] = 0
        mass[residue] = 0
    numbers["*"] = 0
    mass["*"] = 0

    masses = {}
    #TODO
    masses = {masses[chem.elements[i]] : chem.masses[i] for i in range(len(chem.masses))}
    # for i in range(len(chem.masses)):
    #     masses[chem.elements[i]] = chem.masses[i]

    unknown = 0
    for atom in atomlist:
        if atom[1] in numbers:
            numbers[atom[1]] += 1
            mass[atom[1]] += masses[atom[4]]
        else:
            numbers["*"] += 1
            mass["*"] += masses[atom[4]]

    return numbers, mass


def count(atomlist):
    chains = []
    residues = []
    #TODO
    chains = [chains.append(atom[0]) for atom in atomlist]
    for atom in atomlist:
        # chains.append(atom[0])
        residues.append(atom[:3])
    return len(set(chains)), len(set(residues)), len(atomlist)


def analyze_atoms(atomlist):
    chains, residues, atoms = count(atomlist)
    print("Chains:", chains)    
    print("Residues:", residues)    
    print("Atoms:", atoms)    

    num_per_res, mass_per_res = per_residue(atomlist)
    total_mass = sum(mass_per_res.values())
    percentages = {}
    for res in mass_per_res:
        percentages[res] = mass_per_res[res] / total_mass

    print("Total mass:", total_mass)
    print(num_per_res)
    print(mass_per_res)
    print(percentages)


def main(args):
    atoms = read_atoms(args[1])
    analyze_atoms(atoms)    


main(sys.argv)
