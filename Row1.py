A,B=input().split()
A=int(A)
B=int(B)
p=''
q=2
if(A+B<=3):
    for i in range(0,A+B):
        if(i%2!=0):
            p=p+'0'
        else:
            p=p+'1'
else:    
    for i in range(0,A+B):
        if(i==q):
            p=p+'0'
            if(q==B):
                q=q+2
            else:
                q=q+3
        else:
            p=p+'1'
x=len(p)-1
if(int(p[x])==0):
    print('-1')
elif A==1 and B==2: 
     print("011")
else:
    print(p)
