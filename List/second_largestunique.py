num=list(map(int,input().split()))
largest=num[0]
second_largest=largest
for n in num:
    if n>largest:
        largest=n
        if n>second_largest and n!=largest:
            second_largest=n
print(second_largest)