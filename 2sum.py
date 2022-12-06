f = open('test.txt', 'r')
lines=f.readlines()
num_seq = 13
seq_len = 8819


#main algo
def twoSum(nums):
        store  = {}
        for i in range(0,seq_len-1):
            target = 0 - nums[i]
            store[target] = i
        for j in store.keys():
            for i in range(0,seq_len-1):
                if nums[i] == j and i != store[j]:
                    return sorted([i+1,store[j]+1])
        else:
            return [-1]

import sys
sys.stdout = open('output.txt','wt')
for j in range(1,int(num_seq)+1):
    nums = s = list(map(int, filter(None, lines[j].split(' '))))
    converted_list = [str(element) for element in twoSum(nums)]
    joined_string = " ".join(converted_list)
    print(joined_string)
