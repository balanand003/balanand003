A=int(input())
B=list(map(int,input().split()))
c1=[]
v1=1
for i in range(A-1):
    if B[i]<B[i+1]:
        v1+=1
    else:
        c1.append(v1)
        v1=1
c1.append(v1)
print(max(c1))
