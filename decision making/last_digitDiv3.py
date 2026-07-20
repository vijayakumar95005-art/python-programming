num=int(input("Entert the 3 Digit number:"))
n=num//100
num=num%10
if num%3==0:
    print("Last digit is Divisible by 3")
else:
    print("Last digit is not Divisible by 3")
