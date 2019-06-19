P=input()
Q=P[0]
for i in P:
  if (P.count(Q)<=P.count(i)):
    Q=i
print(Q)
