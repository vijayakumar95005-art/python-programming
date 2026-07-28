num=[11,12,44,11,12,44,11]
list1=[]
for i in range(0,len(num)):
    if num[i] not in list1:
        list1.append(num[i])
print(list1)
list2=[]
for i in range(len(num)):
    l=min(num)
    list2.append(l)
    num.remove(l)
print(list2)
print(str(list2[::-1]))
