A = int(input())
B = list(map(int,input().split()))
C,D = 0,[]
P = [x for x in range(1,A+1)]
for i in B:
  if i in P:
    P.remove(i)
Q = 0
for i in range(0,A-1):
  K = B[i]
  for j in range(i+1,A):
    if K == B[j]:
      if K < P[Q]:
        B[j] = P[Q]
        C =C+ 1
      else:
        B[i] = P[Q]
        C =C+ 1
        Q=Q+ 1
print(C)
print(*B)

