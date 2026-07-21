sentence=input()
word=input()
replace_word=input()
if word in sentence:
   print(sentence.replace(word,replace_word))
else:
   print("Word is not found")
