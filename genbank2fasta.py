from Bio import Entrez
from Bio import SeqIO
Entrez.email = "andrewmaltezthomas@gmail.com"
f = open('test.txt', 'r')
lines=f.readlines()
arr = lines[0]
IDs_list = list(map(str, filter(None, arr.split(' '))))

handle = Entrez.efetch(db="nucleotide", id=IDs_list, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
import sys
sys.stdout = open('output.txt','wt')
print()
for i in range(len(records)):
	if len(records[i]) == min([len(record.seq) for record in records]):
			print(">" + records[i].description)
			print (records[i].seq)
