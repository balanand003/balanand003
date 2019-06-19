import sys, string, math

def findSubarrays(ar, n):
    s = 0;
    for i in range(0, n):
        s += ar[i];

    found = False
    lsum = 0
    for i in range(0, n - 1):
        lsum += ar[i]
        rsum = s- lsum

        if lsum * (n - i - 1) == rsum * (i + 1):
            return True
    if found == False:
        return False

n = int(input())
B = [ int(x) for x in input().split()]
if findSubarrays(B, n) :
         print('yes')
else :
                   
     print('no')
