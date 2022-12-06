f=open('test.txt')
lines=f.readlines()
sample = lines[1]
s = list(map(int,sample.split()))
#print(s)
part = s[0]
temp1 = []
temp2 = []
for i in s:
    if i<part:
        temp1.append(i)
    if i>part:
        temp2.append(i)
temp1.append(part)
ans = temp1 + temp2
import sys
sys.stdout = open('output.txt','wt')
for j in ans:
    print(j, end =" ")

