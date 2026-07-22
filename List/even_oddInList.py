numbers = [10, 15, 22, 33, 44, 51]
even=0
odd=0
for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("Even count:",even)
print("Odd count:",odd)