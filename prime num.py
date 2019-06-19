AB,BA = map(int,input().split())
S= 0
for i in range(AB,BA+1):
  if i > 1:
    for J in range(2,i):
      if i % J == 0:
        break
    else:
      s=s+ 1
print(S)
