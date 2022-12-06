#have 2 arr 1 target and sample 
#break from string to arr
f=open('rosalind_bins.txt')
lines=f.readlines()
sample = lines[2]
target = lines[3]
s = list(map(int,sample.split()))
t = list(map(int,target.split()))
ans = []

def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid + 1
 
    # If we reach here, then the element was not present
    return -1
 

for i in t:
    ans.append(binary_search(s,i))
    
import sys
sys.stdout = open('output.txt','wt')
for j in ans:
    print(j, end =" ")




