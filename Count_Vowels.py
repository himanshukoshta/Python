st=input("Enter a string: ")
count=0
s1=st.lower()
for i in s1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)