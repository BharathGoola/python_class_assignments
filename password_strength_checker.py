import time
password=input("enter the password:")
if len(password)<8:
    print("password is too short.password must be contain atleast 8 characters:")
if not any(char.isdigit() for char in password):
    print("password should contain atleast number:")
if not any(char in "!@#$%^&*()-_=+[]{}:;'~" for char in password):
    print("password should contain any one special_character:")
if not any(char.isupper() for char in password):
    print("password should contain any one upper case letter:")

if (
    len(password)>=8 and
    any(char.isdigit() for char in password) and
    any(char in "!@#$%^&*()-_=+[]{}:;'~" for char in password) and
    any(char.isupper() for char in password)
):
    print("strong password")
    