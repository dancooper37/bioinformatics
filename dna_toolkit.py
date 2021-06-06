from collections import Counter
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
    # More pythonic approach
    # return dict(collections.Counter(seq))


def transcription(seq):
    """DNA to RNA translation. Replaces Thymine with Uracil"""
    return seq.replace("T", "U")


def reverse_compliment(seq):
    """Finds complimentary base pairs and reverses list"""
    return "".join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]  # Reverses the list
    # More pythonic approach
    # mapping = str.maketrans("ATCG", "TAGC")
    # return seq.translate(mapping)[::-1]


def gc_content(seq):
    """GC content in DNA/RNA sequence"""
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k = 20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res


def translate_seq(seq, init_pos=0):
    """Translates DNA sequence into amin acid sequence"""
    return [DNA_Codons[seq[pos:pos+ 3]] for pos in range(init_pos, len(seq) - 2, 3)]


def codon_usage(seq, aminoacid):
    """Provides frequency of each codon encoding a given amino acid in DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict


def gen_reading_frames(seq):
    """Generate the six reading frames of a DNA sequence, including the reverse compliment"""
    frames = [
        translate_seq(seq, 0),
        translate_seq(seq, 1),
        translate_seq(seq, 2),
        translate_seq(reverse_compliment(seq), 0),
        translate_seq(reverse_compliment(seq), 1),
        translate_seq(reverse_compliment(seq), 2)
    ]
    return frames


def proteins_from_rf(aaSeq):
    """Finds all possible proteins from an AA sequence in reading frame. Returns list of possible proteins"""
    currentProtein = []
    proteins = []
    for aa in aaSeq:
        # Stop protein list if _ marker found
        if aa[:1] == "_":  # index used to align with structures.py format"
            if currentProtein:
                for p in currentProtein:
                    proteins.append(p)
                currentProtein = []
        else:
            # Start protein list if methionine found
            if aa[:1] == "M":
                currentProtein.append("")
            for i in range(len(currentProtein)):
                currentProtein[i] += aa
    return proteins


def all_proteins_from_rf(seq, startReadPos = 0, endReadPos = 0, ordered = False):
    """Find all possible proteins for all open reading frames"""
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startReadPos:endReadPos])
    else:
        rfs = gen_reading_frames(seq)

    res = []
    for rf in rfs:
        proteins = proteins_from_rf(rf)
        for p in proteins:
            res.append(p)

    if ordered:
        return sorted(res, key = len, reverse = True)
    return res



