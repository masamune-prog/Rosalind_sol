from Bio import SeqIO

count = SeqIO.convert("rosalind_tfsq.txt", "fastq", "output.txt", "fasta")
print("Converted %i records" % count)
