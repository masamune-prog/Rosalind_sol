#Opens FASTA file
from collections import defaultdict
from itertools import product
f = open('test.txt', 'r')

#Creates dictionary
rosDict={}

#Parse over FASTA file
for line in f:

    #Checks for FASTA name and puts it into dictionary
    if line[0]=='>':
        rosDict[line.rstrip('\n')]=''
        index = line.rstrip('\n')

    #Inputs DNA sequence to corresponding FASTA name based on index
    else:
        rosDict[index] = rosDict.get(index)+line.rstrip('\n')

#Returns Dictionary of FASTA names and corresponding DNA sequences
#print(rosDict)

seqlist = list(rosDict.values())

def get_superstring(reads_list,superstring = ''):

    if len(reads_list) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = reads_list.pop(0)
        return get_superstring(reads_list, superstring)

    else:
        for current_read_index in range(len(reads_list)):
            current_read = reads_list[current_read_index]
            current_read_length = len(current_read)

            for trial in range(current_read_length // 2):
                overlap_length = current_read_length - trial

                if superstring.startswith(current_read[trial:]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, current_read[:trial] + superstring)

                if superstring.endswith(current_read[:overlap_length]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, superstring + current_read[overlap_length:])
import sys
sys.stdout = open('output.txt','wt')
result = get_superstring(seqlist)
print(result)


