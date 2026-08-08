n=int(input())
l=[5,2,8,4,7]
for i in range(len(l)):
    for j in range(i+1,len(l)):
       if l[i]+l[j]==n:
          print(l[i],l[j])