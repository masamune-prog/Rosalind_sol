from Bio import Entrez
f = open('test.txt', 'r')
lines=f.readlines()
Entrez.email = "zhenrong004@gmail.com"
organism = lines[0]
organism = organism + "[Organism]"
database = 'nucleotide'
start_date = lines[1]
end_date = lines[2]
handle = Entrez.esearch(db=database, term=organism, datetype='pdat', mindate= start_date, maxdate=end_date)
record = Entrez.read(handle)
print(record["Count"])
