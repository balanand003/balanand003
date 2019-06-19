import sos
a=list(map(int,input()))
b=list(a)
c=[]
for i in range(1,len(a)):
    c=a
    for j in range(len(a)):
        c.pop(j)
        x=""
        for k in range(len(c)): x=x+str(c[k])
        if int(x)%8==0:
            print("yes")
            sys.exit()
        c=list(b)
print("no")
