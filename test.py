f = open('sample.txt', 'r')
percentage = []

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
print(rosDict)

for value in rosDict.values():
    counter = 0
    c_g_highest = 0
    for i in value:
        #dna seq
        #print(i)
        for c in i:
            if c == 'C' or c == 'G':
                counter += 1
    c_g_current = (counter/len(value)) * 100
    percentage.append(c_g_current)
pos = 0
while percentage[pos] != max(percentage):
    pos = pos+1
print(list(rosDict)[pos])
print(max(percentage))
    

        
        
    