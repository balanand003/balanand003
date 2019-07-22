A1,B1=list(map(int,input().split(" ")))
C1=0
for i in range(A1,B1):
       V=(bin(i)[2:]).count("1")
       if(V==1):
            continue
       for i in range(2,V):
               if(V%i==0):
                   flag=False
                   break
       else:
          C1=C1+1
print(C1)
