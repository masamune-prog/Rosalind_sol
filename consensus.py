#Opens FASTA file
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
lenght = len(rosDict['>Rosalind_4110'])
dict = {
'A':[0]*lenght,
'C':[0]*lenght,
'G':[0]*lenght,
'T':[0]*lenght
}

for i in rosDict.values():
    for j in range(len(i)):
        if i[j] == 'A':
            dict['A'][j] += 1
        if i[j] == 'C':
            dict['C'][j] += 1
        if i[j] == 'T':
            dict['T'][j] += 1
        if i[j] == 'G':
            dict['G'][j] += 1

#print(dict)

#find max of each array
seq = ''
temp = ''
for i in range(lenght):
    temp_val = max(dict['A'][i],dict['T'][i],dict['G'][i],dict['C'][i])
    temp = ''
    for letter in dict.keys():
        if temp_val == dict[letter][i]:
            temp = letter
    seq += temp
import sys
sys.stdout = open('output.txt','wt')
print(seq)
for base in dict.keys():
    print(base + ': ', end = '')
    for num in dict[base]:
        print(num, end = ' ')
    print()
