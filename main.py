from DNAToolkit import *
from utilities import colored
import random

# Creates random DNA sequence for testing
randDNAStr = "".join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"[1] + Sequence Length: {len(DNAStr)}\n")
print(colored(f"[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n"))

print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n")

print(f"[4] + DNA String + Reverse Compliment:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_compliment(DNAStr))} 5'\n")

