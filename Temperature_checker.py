import time
temperature=float(input("enter the temperature in °c:"))
if temperature<=15:
    print("temperature is cool:")
if temperature>=35:
    print("temperature is too hot:")
if temperature>=15 and temperature<=35:
    print("temperature is normal:")