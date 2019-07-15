A,B = map(int,input().split())
C = list(map(int,input().split()))
v,w = 0,[]
for i in range(0,len(C)):
  t = i
  for X in range(0,len(C)):
    for l in range(0,B):
      if l == B-1:
        try:
          v += C[X+i]
        except IndexError:
            t = t-1
            v =v+C[t]
      else:
        v =v+ C[i]
    w.append(v)
    v = 0
for i in range(0,len(C),B):
  v = sum(C[i:i+B])
  w.append(v)
print(*sorted(set(w)))
