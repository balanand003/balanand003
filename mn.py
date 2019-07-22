A,B=map(int,input().split())
X=[]
for i in range(A):
  C=set(map(int,input().split()))
  X.append(C)
ro=C.intersection(*X)
print(*ro)
