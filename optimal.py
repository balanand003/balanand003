A=int(raw_input())
B=list(map(int,raw_input().split()))
B.sort()
x=0
y=0
for i in range(len(B)):
    if B[i]>=s:
        y=y+1
    x=x+B[i]
print(y)
