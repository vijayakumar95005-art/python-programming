grade=int(input())
if grade>=90 and grade<=100:
    print("A")
elif grade>=80 and grade<=89:
    print("B")
elif grade>=70 and grade<=79:
    print("C")
elif grade<70:
    print("Fail")
else:
    print("Invalid")