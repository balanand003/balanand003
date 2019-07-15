A=int(input())
B=3
C=3
X=1
for X in range(A-1):
    if(B==1):
        B=C*2
        C=B
    else:
        B=B-1
print(B)   
