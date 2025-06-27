import time
username=input("enter the username:")
password=int(input("enter the password:"))
if username=="Bharath" and password==1234:
    print("login successfully:")

if username!= "Bharath" or password!= 1234:
    print("Please enter the correct username or password:")
print()
time.sleep(2)
print("end of an application")
