A=int(raw_input())
B=0
C=0
D=[]
while B<90 and B<N:
  r=0
  for j in str(A-i):
    r+=int(j)
  if r+(A-B)==A:
    C+=1
    D.append(A-i)
  B=B+1
print(C)
for B in D:
  print(B)
