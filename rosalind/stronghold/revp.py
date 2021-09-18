from toolkit.dna import reverseCompliment
from toolkit.utilities import unpackFASTAToStr

DNAStr = unpackFASTAToStr("../compute_data/rosalind_revp.txt")
print(DNAStr)
print(reverseCompliment(DNAStr))