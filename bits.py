A=int(input())
B=[]
C=bin(2**A-1)[2::]
x=len(C)
for i in range(0,2**A):
	m=bin(i)[2::]
	if len(m)<li:
		B.append([m.count("1"),(x-len(m))*"0"+m])
	else:
		B.append([m.count("1"),m])
B.sort()
for i in range(0,len(B)):
	print(B[i][1])
