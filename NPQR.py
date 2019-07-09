A,B,C,D=map(int,input().split())
P=[int(i) for i in input().split()]
Q=[B*P[i]+C*P[j]+D*P[k] for i in range(len(P)) for j in range(len(P)) for k in range(len(P)) if i<=j<=k]
print(max(Q))
