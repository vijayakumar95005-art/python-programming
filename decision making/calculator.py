a=int(input("Enter the First value:"))
b=int(input("Enter the second value:"))
print("1.Add\n2.Subtraction\n3.Multiplication\n4.Division")
num=int(input("Enter the choice:"))
if num==1:
    print("Addition:",a+b)
elif num==2:
    print("subtraction:\n",a-b)
elif num==3:
    print("Multiplication:",a*b)
elif num==4:
    if b==0:
        print("ZeroDivision Error")
    else:
        print("Division:",a/b)
        print("Floor Division:",a//b)
        print("Modulus:",a%b)
else:
    print("Invalid Choice!")