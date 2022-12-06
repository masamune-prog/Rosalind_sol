#extract the line to arr
f=open('test.txt')
lines=f.readlines()
sample = lines[1]
s = list(map(int, filter(None, sample.split(' '))))
part = s[0]
smaller = []
larger = []
equal = []
for i in s:
    if i<part:
        smaller.append(i)
    if i>part:
        larger.append(i)
    if part == i:
        equal.append(i)
#print(larger)
#print(equal)
#print(smaller)
smaller.extend(equal)
smaller.extend(larger)
#print(smaller)
import sys
sys.stdout = open('output.txt','wt')
for j in smaller:
    print(j,end = " ")
