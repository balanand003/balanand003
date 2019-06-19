a,b= map(int,input().split())
x1={int(x) for x in input().split()}
x2={int(y) for y in input().split()}
if((x2.issubset(x1))):
  print("YES")
else:
  print("NO")
