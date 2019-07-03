A,B=list(map(int,input().split()))
C,D=list(map(int,input().split()))
E,F=list(map(int,input().split()))
if (A==C==E or B==D==F or(A==B and C==D and E==F)):
    print ("yes") 
else: 
    print ("no")
