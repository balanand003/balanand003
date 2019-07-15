A=input()
B=''
C=[]
for i in A:
    if i not in C:
        B=B+i
        C.append(i)
    elif i in C:
        break
print(len(C))
