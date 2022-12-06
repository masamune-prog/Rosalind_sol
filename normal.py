m = 6
def mortal(m):
    n =3
    if m==1 or m==2:
        return 1
    if m == 3:
        return n+1
    else:
        ans = n*mortal(m-2) + (mortal(m-1))
        return ans
print(mortal(m))
