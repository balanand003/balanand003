A=input()
B=[]
for i in range(0,len(A)-1):
  for j in range(i+1,len(A)):
    temp=A[i:j+1]
    len1=temp[::-1]
    if temp==len1:
      B.append(len(A)-len(len1))
print(min(B))
