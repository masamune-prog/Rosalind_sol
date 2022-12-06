def findstem(arr):

    # Determine size of the array
    n = len(arr)

    # Take first word from array
    # as reference
    s = arr[0]
    l = len(s)

    res = ""

    for i in range(l):
        for j in range(i + 1, l + 1):

            # generating all possible substrings
            # of our reference string arr[0] i.e s
            stem = s[i:j]
            k = 1
            for k in range(1, n):

                # Check if the generated stem is
                # common to all words
                if stem not in arr[k]:
                    break

            # If current substring is present in
            # all strings and its length is greater
            # than current result
            if (k + 1 == n and len(res) < len(stem)):
                res = stem

    return res
 #Creates dictionary
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
ans = findstem(array)
print(ans)
