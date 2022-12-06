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
print(rosDict)

def findsubstring(s1,s2):
    ans = ""
    len1 = len(s1)
    len2 = len(s2)
    for i in range(len1):
        for j in range(len2):
            temp = 0
            match = ''
            while ((i+temp < len1) and (j+temp<len2) and s1[i+temp] == s2[j+temp]):
                match += s2[j+temp]
                temp+=1
            if (len(match) > len(ans)):
                ans = match
    return ans
    '''
    if len(ans) >= 3:
        return True
    else:
        return False
    '''

entry = []
#create list of keys:
keys = list(rosDict.keys())
for i in keys:
    for j in keys:
        if i == j:
            continue
        if findsubstring(rosDict[i][:-3],rosDict[j][3:]) == True and ([i,j] and [j,i]) not in entry:
            print([rosDict[i][:-1],rosDict[j][1:]])
            entry.append([i,j])
            print(findsubstring(rosDict[i],rosDict[j]))
for i in entry:
    print(i)


#print(findsubstring(rosDict['>Rosalind_0442'],rosDict['>Rosalind_5013']))
