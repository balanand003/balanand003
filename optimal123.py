A,B=map(int,input().split())
X=list(map(int,input().split()))
if B==1:
    print(min(X))
elif B==2:
    print(max(X[0],X[A-1]))
else:
    print(max(X))
