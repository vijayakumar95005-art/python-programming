numbers = list(map(int,input().split()))
largest=numbers[0]
second_largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
for num in numbers:
    if num>second_largest and num!=largest:
        second_largest=num
print(second_largest)


