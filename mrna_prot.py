from rna_codon import RNA_codon_table
f = open('input.txt','r')
lines = f.readlines()
protein = str(lines[0]).rstrip('\n')
#num ways to encode first * num ways to encode next ... * 3(ways to stop codon) %1000000
print(protein)
def ways_encode(n):
    return len(RNA_codon_table[n])
counter = 1
for i in protein:
    print(i)
    counter *= ways_encode(i)
counter = counter * 3
print(counter%1000000)
