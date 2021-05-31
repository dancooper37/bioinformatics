from dna_toolkit import *
from utilities import colored
import random
import time

start_time = time.time()

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

print(f"[8] + Codon Frequencies\n")
for i in DNA_Codons_List:
    print(f"      [{i}] = {codon_usage(DNAStr, i[:1])}")

print(f"\n[9] + Reading frames:\n")
for frame in gen_reading_frames(DNAStr):
    print(frame)

print(f"\n[END] Execution Time: {round(time.time()-start_time, 4)} seconds ")


