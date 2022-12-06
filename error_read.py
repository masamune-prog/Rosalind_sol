from Bio.Seq import Seq
rosDict={}
f = open('input.txt', 'r')
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
array = list(rosDict.values())
#print(array)
correct = []
wrong = []
arr_cpy = array.copy()
#find those that are correct
l = len(array)
def rev_compl(st):
    nn = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(nn[n] for n in reversed(st))
for i in range(0,l-1):
    #find the wrong sequence
    target = array[i]
    rev = rev_compl(target)
    #print([target,rev])
    #ccover
    print(array[i+1:])
    if (target not in array[i+1:]):
        #print(target)
        wrong.append(target)
print(wrong)
