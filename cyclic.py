A, B = map(int,raw_input().split())
C = map(int,raw_input().split())
for i in range(B):
 D = C[-1]
  for j in range(len(C)-2,-1,-1):
    C[j+1] = C[j]
  C[0] = D
for i in range(len(C)):
  print C[i],
