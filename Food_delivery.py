import time
order_amount=int(input("enter the amount:"))
if order_amount>=249:
    print("congratulations! you got a free_delivery:")
if order_amount<249:
    print("sorry! you are not eligible for free_delivery,order more:")
print()
time.sleep(2)

print("end of an application")