A=input().split()
B=int(A[1])
C=int(A[0])
D=[int(P) for P in A[0]]
X=0
y=1;
while(X==0):
	prod=y*C
	l=[ int(P) for P in str(prod)]
	k=0
	j=len(l)-1
	while(l[j]==0):
		k=k+1
		j=j-1
	if(k>=B):
		print(prod)
		X=1
	y=y+1
