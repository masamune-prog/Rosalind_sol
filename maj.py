f=open('rosalind_maj.txt')
lines=f.readlines()
hashmap_i = {}
num_arr = lines[0][0] + lines[0][1]
for i in range(1,int(num_arr)+1):
    s = list(map(int, filter(None, lines[i].split(' '))))
    hashmap_i.clear()
    for j in s:
        if j not in hashmap_i:
            hashmap_i[j] = 1
        else:
            hashmap_i[j] = hashmap_i[j] + 1
    #check hashmap for val more than half
    #print(hashmap_i)
    if max(hashmap_i.values()) <= len(s)/2:
        print(-1,end = " ")
    else:
        print(max(hashmap_i, key=hashmap_i.get),end = " ")
