A= int(input())
C=['a','e','i','o','u','A','E','I','O','U']
B = input()
for j in range(0,len(C)):
    B= B.replace(C[j],'')
print(B[::-1])
