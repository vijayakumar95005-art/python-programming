num=list(map(int,input().split()))
print(max(num))#using built in functions
largest=num[0]#without using built in functions
for n in num:
    if n>largest:
        largest=n
print(largest)