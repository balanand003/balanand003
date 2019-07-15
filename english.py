A,B=map(str,input().split("|"))
t=input()
if  len(A)>len(B):
    if len(A)==len(B)+len(t):
        print(A+"|"+B+t)
elif len(A)<len(B):
     if len(B)==len(A)+len(t):
        print(A+t+"|"+B)
elif len(A)==len(B) and len(t)>1 or (len(B) or len(A)):
    print("impossible")
