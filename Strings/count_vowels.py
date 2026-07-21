word=input()
count=0
lower_case=word.lower()
for i in range(0,len(word)):
    if lower_case[i] in "aeiou":
       count+=1
print(count)
