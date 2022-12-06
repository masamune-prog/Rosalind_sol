import itertools
import sys
f = open('input.txt','r')
data = f.readlines()
arr = data[0]
letters = list(map(str, filter(None, arr.split(' '))))
new_letters = []
for i in letters:
    new_letters.append(i.strip())
lenght = int(data[1])
perm = itertools.product(new_letters,repeat = lenght)
output = []
for i , j in enumerate(list(perm)):
    permutate = ''
    for item in j:
        permutate += str(item)
    output.append(permutate)
output.sort()
print(output)
sys.stdout = open('output.txt','wt')
for i in range(0,len(output)):
    print(output[i])
