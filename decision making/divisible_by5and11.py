n=int(input())
if n%5==0 and n%11==0:
    print("number is divisible by both 5 and 11")
elif n%5==0:
    print("number is divisible by 5")
elif n%11==0:
    print("number is divisible by 11")