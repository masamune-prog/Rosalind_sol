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
seq = str(list(rosDict.values())[0])
def init_arr(seq):
    arr = [0]*len(seq)
    arr[0] = 0
    for i in range(1,len(seq)):
        j = arr[i-1]
        while j > 0 and seq[i] != seq[j]:
            print(seq[i])
            j = arr[j-1]
            print(j)
        if seq[i] == seq[j]:
            j += 1
        arr[i] = j
    return arr
#import sys
#sys.stdout = open('output.txt','wt')
ans = init_arr(seq)
for a in ans:
    print(a,end = ' ')
