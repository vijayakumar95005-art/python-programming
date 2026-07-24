num=list(map(int,input().split()))
maxn=0
for i in num:
    n=num.count(i)
print(n)
if maxn<n:
    maxn=n
    print(i,":",maxn)