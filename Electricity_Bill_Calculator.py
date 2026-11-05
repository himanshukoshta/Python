unit=int(input("Enter the unit:"))
amount=0
if unit<0:
    print("Invalid units")
elif unit<=100:
    amount+=unit*5
    print(amount)
elif unit<=200:
    amount+=100*5
    amount+=(unit-100)*7
    print(amount)
else:
    amount+=100*5
    amount+=100*7
    amount+=(unit-200)*10
    print(amount)
