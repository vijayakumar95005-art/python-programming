num=list(map(int,input().split()))
flag=0
for i in range(len(num)):
    if num[i]==num[-i-1]:
       flag=1
    else:
       flag=0
       break
if flag==1:
    print("Palindrome")
else:
    print("Not palindrome")