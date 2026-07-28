str=input()
vowel=""
cons=""
for ch in str:
    if ch.lower() in "aeiou":
        vowel+=ch
    else:
        cons+=ch
print(cons+vowel)

