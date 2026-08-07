s=input()
print(s[:8],end=" ")
n=float(s[9:11])
t1=n-05.30
m=float(s[12:])
t2=m/100
time=t1+t2
if time<=12:
    print(f"{time:.2f}")
else:
    print(f"{time-12.00:.2f}")


