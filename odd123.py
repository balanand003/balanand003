A = input()
B = list(A)
B[::2], B[1::2] = B[1::2], B[::2]
C=''.join(B)
print(C)
