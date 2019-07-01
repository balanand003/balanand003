t1,s1=map(int,input().split())
n1=0
Li=[]
for x in range(t1):
      Li.append(input())
for x in range(t1):
      for y in range(s1-1):
            if(Li[x][y]!='R' and Li[x][y+1]!='R'):
                  n1=n1+3
            elif(Li[x][y]!='G' and Li[x][y+1]!='G'):
                  n1=n1+5
print(n1)
