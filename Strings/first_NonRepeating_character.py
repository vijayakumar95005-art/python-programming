#First non-repeating character with using count()
str=input()
for b in str:
    if str.count(b)==1:
        print(b)
        break

#First non-repeating character without using count()
freq={}
for ch in str:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
found=False
for ch in str:
    if freq[ch]==1:
        print(ch)
        found=True
        break
if not found:
    print("No non repeating character")    