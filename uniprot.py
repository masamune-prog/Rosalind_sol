from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('Q5SLP9') #you can give several IDs separated by commas
record = SwissProt.read(handle)
bio_proc = []
for item in record.cross_references:
    if item[0] == 'GO' and item[2][0]=='P':
        bio_proc.append(item[2].lstrip('P:'))

print('\n'.join(bio_proc))
