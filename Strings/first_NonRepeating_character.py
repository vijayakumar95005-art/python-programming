str=input()
for b in str:
    if str.count(b)==1:
        print(b)
        break

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