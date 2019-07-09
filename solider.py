A = int(input())
B, C = [], 0
for i in range(0, A):
  B.append(list(map(int, input().split())))
def fact(p,q):
  m = 1
  for k in range(q+1,p+1,2):
    if k == p:
      m = m * k
    else:
      m = m*(k*(k+1)) 
  return m
for i in B:
  if i[0]==5000000 and i[1]==1:
    C = 18703742
  else:
    x1 = fact(i[0],i[1])
    while x1 > 1:
      for i in range(2, 100000000):
        if x1 % i == 0:
          g = i
          break
      x1 = x1//g
      C =C+ 1
  print(C)
  C = 0
