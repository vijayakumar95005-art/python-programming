num=list(map(int,input().split()))
n=int(input())
for l in num:
    if l==n:
        num.remove(n)
print(num)
    