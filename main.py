from dna_toolkit import *
from utilities import colored
import random

# Creates random DNA sequence for testing
randDNAStr = "".join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"[1] + Sequence Length: {len(DNAStr)}\n")
print(colored(f"[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n"))

print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n")

print(f"[4] + DNA String + Compliment + Reverse Compliment:\n\n    5' {colored(DNAStr)} 3'")
print(f"       {''.join(['|' for c in range(len(DNAStr))])}")
print(f"    3' {colored(reverse_compliment(DNAStr)[::-1])} 5' (Compliment)")
print(f"    5' {colored(reverse_compliment(DNAStr))} 3' (Reverse Compliment)\n")

print(f"[5] + GC Content in DNA: {gc_content(DNAStr)}%\n")
print(f"[6] + GC Content in Subsection k = 5 of DNA: {gc_content_subsec(DNAStr, k = 5)}\n")

print(f"[7] + Amino Acid Sequence from DNA: {' '.join(translate_seq(DNAStr))}\n")

print(f"[8] + Codon frequency (L): {codon_usage(DNAStr, 'L')}\n")
