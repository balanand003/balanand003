A1,B1=map(int,input().split())
C1=list(map(int,input().split()))
X=[[abs(i1-B1),i1]for i1 in C1]
X.sort()
X=X[1:]
X=[i1[1] for i1 in X[:3]]
print(*X)
