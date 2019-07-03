A=input()
B="dhoni"
C=0
if(len(A)==5):
    for i in range(0,len(B)):
        if(A[i] in B):
            C=C+1
    if(C==5):
        print("yes")
    else:
        print("no")
else:
    print("no")
