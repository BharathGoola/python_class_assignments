import time
bank_balance=float(input("enter a bank_balance₹:"))
purchase_amount=float(input("enter purchase amount₹:"))

if bank_balance>=purchase_amount:
    print("payment successfull")
    print("remaining amount₹:",bank_balance-purchase_amount)


if bank_balance<purchase_amount:
    print("insufficient balance.please add money.")


                         
                         
                         
                         
                   