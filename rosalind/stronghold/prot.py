# Find protein in RNA string

from toolkit.dna import translateRNASeq, proteinScan

with open("../test_data/prot.txt", "r") as f:
    seq = f.readline()


proteinList = translateRNASeq(seq)
print("".join(proteinList))



