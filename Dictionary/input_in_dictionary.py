n=int(input())
k={}
for i in range(1,n):
    m=i+97
    v={i:chr(m)}
    k.update(v)
print(k)
