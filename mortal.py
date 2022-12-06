'''
6 3
m is life of rabbits
n is duration of experiment
1 -> 1 -> 1 -> 2 -> 4 -> 4
1st month only 1 rabbits
2nd month mature 1 pair
3rd month 1 pair is born and another dies
4th month 1 pair is born 1 + 1 = 2
5th month 2 pairs born 1 dies 2+2-1 = 3
6th month 1 pair born 3+1 = 4
'''
def fibo(month,age):
    memo = [0]*age
    memo[0] = 0
    memo[1] = 1
    for i in range(2,month):
        temp = list(memo)
        memo[0] = sum(memo[1:])
        for j in range(1,age):
            memo[j] = temp[j-1]
    return sum(memo)

print(fibo(80,20))
