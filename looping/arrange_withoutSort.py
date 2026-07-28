"""
num=[1,17,281,32,64,91]
list1=[]
for i in range(len(num)):
    l=min(num)
    list1.append(l)
    num.remove(l)
print(list1)
"""

num=[1,17,281,32,64,91]
list1=[]
for i in range(len(num)):
    for j in range(len(num)):
        if num[j]<=num[i]:
            list1.append(num[j])
            num.pop(num[j])
print(list1)