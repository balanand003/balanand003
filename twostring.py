A,B=map(str,input().split())
c1=0
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if A[i]==B[j]:
            c1=c1+1
if c1>=2:
    print("yes")
else:
    print("no")
