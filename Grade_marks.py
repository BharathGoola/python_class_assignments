import time
Marks=int(input("Enter the marks:"))
if Marks>=90:
    print("congratulations! you got Grade A marks:")
if 65>=Marks<90:
    print("you got Grade B marks:")
if 38>=Marks<65:
    print("you got Grade C marks:")
if Marks<38:
    print("you fail! betterluck try next time:")
print()
time.sleep(2)
print("end of an application")
