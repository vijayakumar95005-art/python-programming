str=input()
str1=str.split()
largest=str1[0]
for s in str1:
    if len(s)>len(largest):
        largest=s
print(largest)


