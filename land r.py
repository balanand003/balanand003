A=list(map(int,input().split()))
for i in range(1,(A[0]*A[1])+1):
    if(i%A[0]==0 and i%A[1]==0):
        print(i)
        break
