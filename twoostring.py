A = input()
B = input()
de_str = ''
C = []
for i in range(26):
    C.append(chr(i+97))

for i in range(len(B)):
    B_pos = C.index(B[i]) + 1
    A_pos = C.index(A[i]) + 1
    if A_pos + B_pos > 26:
        pos = A_pos - (26 - B_pos)
        de_str =de_str+ C[pos-1]
    else:
        pos = A_pos + B_pos
        de_str =de_str+ C[pos-1]
print(de_str)
