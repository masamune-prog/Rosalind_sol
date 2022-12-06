counter = 0
f=open('test.txt')
lines=f.readlines()
sample = lines[1]
s = list(map(int,sample.split()))
for i in range(1,len(s)):
    key = s[i]
    j = i-1
    while j >= 0 and key < s[j]:
        s[j+1] = s[j]
        j-=1
        counter = counter + 1
    s[j+1] = key
#print(s)
print(counter)