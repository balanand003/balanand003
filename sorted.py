A=int(input())
for i in range(2,A+1):
    if(A%i==0):
        B=0
        for j in range(1,i+1):
            if(i%j==0):
                B=B+1
        if(B==2):
            print(j,end=" ")
