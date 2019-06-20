A=input()
B=len(A)
C=[]
r=""
for i in A:
    C.append(i)
for i in range(B):
    r=r+l.pop()
if r==A:
    print('YES')
else:
    print('NO')
