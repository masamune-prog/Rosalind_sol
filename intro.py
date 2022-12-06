import math
f=open('test.txt')
lines=f.readlines()
seq = str(lines[0])[:-1]
sample = lines[1]
s = list(map(float, filter(None, sample.split(' '))))
output = []
#print(seq)
#print(s)
prob = 0
for i in s:
    prob = 0
    chance = {
        'A' : (1-i)/2
        'C' : i/2,
        'G' : i/2,
        'T' : (1-i)/2
    }
    for j in seq:
        print(prob)
        prob = prob + math.log10(chance[j])

    output.append(round(prob,3))
import sys
sys.stdout = open('output.txt','wt')
for ans in output:
    print(ans, end = ' ')
    