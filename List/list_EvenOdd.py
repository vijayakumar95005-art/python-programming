num=list(map(int,input().split()))
even=[]
odd=[]
for n in num:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)
print(min(even),max(even))
print(min(odd),max(odd))
