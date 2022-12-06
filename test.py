import itertools
n = 6
permutation = []
nr = 0
for i in itertools.permutations(list(range(1, n + 1))):
    for j in itertools.product([-1, 1], repeat=len(list(range(1, n + 1)))):
        perm = [a * sign for a, sign in zip(i, j)]
        permutation.append(perm)
        nr += 1

print(nr)

for i in range(len(permutation)):
    print(*permutation[i], sep=' ')
