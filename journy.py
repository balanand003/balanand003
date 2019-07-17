A, B, C, D = map(int, input().split())
coun = 0
u= B-C
if (u >= 0):
    q= (A-C)*2
    for i in range (D):
        if (i == D-1):
             q =q/ 2
        if (u< q):
            u= B
            coun =coun+ 1
        u = u - q
        if (u < 0):
            coun = -1
            break
        q= 2*A - q
    print (coun)
else:
    print (-1)

