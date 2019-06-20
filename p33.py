from itertools import permutations
A=str(input())
A1=permutations(A)
for j in list(set(A1)):
    print(''.join(j))
