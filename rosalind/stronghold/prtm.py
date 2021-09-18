from toolkit.structures import AA_Masses

with open("../compute_data/rosalind_prtm.txt", "r") as f:
    protein = f.readline()

print(protein)

totalMass = 0

for base in protein:
    totalMass += AA_Masses.get(base)

print(totalMass)
