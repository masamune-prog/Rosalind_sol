f=open('test.txt')
lines=f.readlines()
sample = lines[1]
s = list(map(int,sample.split()))
#2 pointer app
p1 = 0
p2 = 1
counter = 0
while p2 != len(s):
    if s[p2] >= s[p1]:
        p1 = p2
        p2 = p2 + 1
    else:
        counter = counter + 1
        p2 = p2 + 1

print(counter)