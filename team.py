A,B=map(int,input().split())
C=list(map(int,input().split()))
C=sorted(C)
t,i=0,0
f=0
while i<len(C)-2:
  x,y,z=C[i:i+3]
  for j in range(0,B):
    x,y,z=x+1,y+1,z+1 
    if x<=5 and y<=5 and z<=5:
      f=1
    else:
      f=0
  if f==1:
    t=t+1
  i=i+3
   
print(t)
