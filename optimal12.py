A,B=map(int,input().split())
C=list(map(int,input().split()))
if B==1:
    print(min(C))
elif B==2:
    print(max(c[0],C[A-1]))
else:
    print(max(C))
