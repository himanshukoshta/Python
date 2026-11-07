s = input("Enter string: ")
count=0
in_word=False
for i in s:
    if i==" ":
        in_word=False
    elif not in_word:
        count+=1
        in_word=True
print(count)