f=open('test.txt')
lines=f.readlines()
sample = lines[1]
#pos = lines[2]
s = list(map(int, filter(None, sample.split(' '))))
s.sort()
import sys
sys.stdout = open('output.txt','wt')
for j in s:
    print(j,end = " ")
