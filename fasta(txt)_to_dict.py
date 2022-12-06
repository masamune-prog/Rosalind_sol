
#Opens FASTA file
#workfile = input("test")
f = open('sample.txt', 'r')

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