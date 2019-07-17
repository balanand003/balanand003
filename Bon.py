A,B= map(int,input().split())
C = list(map(int,input().split()))
p = int(input())
val = (sum(C)-C[B])//2
if p == val:
    print("Bon Appetit")
else:
    print(p-val)
