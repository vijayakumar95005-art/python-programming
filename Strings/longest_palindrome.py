str=input()
center=len(str)//2
for i in range(0,center):
    if str[center+i]==str[center-i]:
        print(str[center+i],end="")
   


