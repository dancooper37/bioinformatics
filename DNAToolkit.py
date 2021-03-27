import collections
from structures import *

def validateSeq(dna_seq):
    """Checks if string is valid DNA sequence"""
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    """Counts nucleotide occurence in a sequence"""
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))


def transcription(seq):
    """DNA to RNA translation. Replaces Thymine with Uracil"""
    return seq.replace("T", "U")


def reverse_compliment(seq):
    """Finds complimentary base pairs and reverses list"""
    return "".join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]  # Reverses the list
