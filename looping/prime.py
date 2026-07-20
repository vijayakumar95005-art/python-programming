n=int(input())
isPrime=True
for i in range(2,n//2+1):
    if n%i==0:
        isPrime=False
        break
if(isPrime):
    print("Prime")
else:
    print("Not a prime")