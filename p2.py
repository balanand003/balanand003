A,B=map(int,input().split())
C=[]
for i in range(0,min(A,B)):
    d=list(map(int,input().split()))
   C.append(d)
for i in range(0,min(A,B)):
    r=[]
    for j in range(0,len(C[i])):
        r.append(C[i][j])
    C[i]=(sorted(r))
for i in range(0,max(A,B)):
    r=[]
    for j in range(0,min(A,B)):
        r.append(C[j][i])
    r=sorted(r)
    for l in range(min(A,B)): C[l][i]=r[l]
for i in range(0,min(A,B)):
    print(*C[i])
