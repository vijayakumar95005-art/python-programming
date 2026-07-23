num=list(map(int,input().split()))
new_list=[]
num_list=[]
for n in num:
    i=0
    if n!=0:
        new_list.append(n)
    else:
        num_list.append(i)
print(new_list)
print(num_list)
new_list.extend(num_list)
print(new_list)

