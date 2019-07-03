A=int(input())
B=[int(i) for i in input().split()]
C=0
for i in range(1,A-1):
	if B[i]<B[i-1] and B[i]<B[i+1]:
		C=C+1
	elif B[i]>B[i-1] and B[i]>B[i+1]:
		C=C+1
print(C)
