A=int(input())
B=list(map(int,input().split()))
C=[]
D1=1
for i in B:
  if i not in C:
    C.append(i)
for i in range(len(C)-1):
  if (C[i]<C[i+1]):
    D1+=1
print(D1)
