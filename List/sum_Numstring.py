n=input().split()
number=[]
string=""
for l in n:
    if l.isdigit():
        number.append(int(l))
    elif l.isalpha():
        string+=l
print(string)
print(number)
print(type(number))
print(type(string))