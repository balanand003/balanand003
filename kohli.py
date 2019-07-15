A,B=map(int,input().split())
C=list(map(int,input().split()))
count=0
for i in C:
  ans=86400-i
  res=B-ans
  count=count+1
  if res<=0:
    break  
print(count)
