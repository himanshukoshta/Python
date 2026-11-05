amount=int(input("Enter amount: "))
final_amount=0
if amount<0:
    print("Invalid amount")
elif amount<1000:
    print("No Discount\n",amount)
elif amount<5000:
    final_amount+=amount-(amount*0.1)
    print("Discount: ",amount*0.1)
    print("Final Amount: ",final_amount)
elif amount<10000:
    final_amount+=amount-(amount*0.2)
    print("Discount: ",amount*0.2)
    print("Final Amount: ",final_amount)
else:
    final_amount+=amount-(amount*0.3)
    print("Discount: ",amount*0.3)
    print("Final Amount: ",final_amount)