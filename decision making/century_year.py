year=int(input())
if year%100==0:
    century=year//100
else:
    century=year//100+1
print("Century:",century)