A=int(input())
B=list(map(int, input().split()))[:A]
C=max(B)
u=[]
for i in range(0,len(B)):
    new=B[i:]
    v=max(new)
    if(B[i]==v):
        u.append(B[i])
print(*u)
print(C)
