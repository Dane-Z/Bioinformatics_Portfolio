from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP


#Read in and Parse PDB file to obtain DSSP --> secondary structure determination
#follows the basic outline on biopython.org -- tutorial
parse = PDBParser()
struc = parse.get_structure('6hrc', "6hrc.pdb")
model = struc[0]
dssp = DSSP(model, '6hrc.pdb')
sec_struc = ''
a_helix = 0
b_sheet = 0
other = 0
none = 0

key = list(dssp.keys())[2]

dssp[key]

for c in range(len(dssp)):
    key = list(dssp.keys())[c]
    sec_struc += dssp[key][2]
    if dssp[key][2] == "H" or dssp[key][2] == "G" or dssp[key][2] == "I":
        a_helix += 1
    if dssp[key][2] == "E" or dssp[key][2] == "B":
        b_sheet += 1
    if dssp[key][2] == "-":
        none += 1
    else:
        other += 1
        

#Prints Summary of secondary structure
#and residue distribution for each structure
print("Protein Model: 6hrc")
print(sec_struc)
print("Residues per structure:")
print("A-helix:", a_helix, "B-sheet:", b_sheet, "Turn/Other:", other, "None determined:", none)
