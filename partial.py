f = open('test.txt', 'r')
lines=f.readlines()
arr = lines[1]
s = list(map(int, filter(None, arr.split(' '))))
s.sort()
numElements = int(lines[2])
import sys
sys.stdout = open('output.txt','wt')
for i in range(0,numElements):
    print(s[i],end = ' ')
