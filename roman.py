A=input()
B = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
C = 0
for i in range(len(A)):
	if i > 0 and B[A[i]] > B[A[i - 1]]:
		C = C+ B[A[i]] - 2 * B[A[i - 1]]
	else:
		C = C+ B[A[i]]
print (C)
