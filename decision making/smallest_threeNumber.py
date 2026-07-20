a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a<b and a<c:
    print("a is smaller ")
elif b<c and b<a:
    print("b is smaller")
else:
    print("c is smaller")