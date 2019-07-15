A1=int(input())
B1=[]
C1=A1//2+A1
for i in range(1,A1+1):
    if i%2==0:
        B1.append(i)
for i in range(1,A1+1):
    if i%2!=0:
        B1.append(i)
for i in range(1,A1+1):
    if i%2==0:
        B1.append(i)
print(C1)
print(*B1)
