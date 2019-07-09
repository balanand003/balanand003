A=input()
if A==A[::-1]:
    print("yes")
else:
    val=A.strip("0")
    if val==val[::-1]:
        print("yes")
    else:
        val=A.lstrip("0")
        if val==val[::-1]:
            print("yes")
        else:
            print("no")
