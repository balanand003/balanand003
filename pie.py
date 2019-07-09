P=int(input())
Q=list(map(int,input().split()))
A_ha=0
B_ha=0
Q.sort(reverse=True)
for i in Q:
  T=A_ha+i
  if B_ha>T:
    A_ha=T
  else:
    A_ha=B_ha
    B_ha=T
print(A_ha,B_ha)
