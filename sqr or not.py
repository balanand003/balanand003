A,z1=list(map(int,input().split()))
B,z2=list(map(int,input().split()))  
C,z3=list(map(int,input().split()))  
D,z4=list(map(int,input().split())) 
p=z2-z1
q=z3-z4
s=C-B
t=D=A
if(p==q==s==t):
  print("yes")
else:
  print("no")
