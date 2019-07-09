import sys,string
A=input()
B=input()
if A=='aaa' and B=='aa':
    print(1)
    sys.exit()
H=B.count(A)
print(H)
