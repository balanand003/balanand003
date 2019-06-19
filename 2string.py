A,B=map(str,input().split())
C={}
D=0
for i in range(len(A)):
    if(A[i] not in C.keys()):
        C[A[i]]=B[i]
    else:
        if(C[A[i]]==B[i]):
            continue
        else:
            D=D+1
if(D==1 or D==0):
    print("yes")
else:
    print("no")
