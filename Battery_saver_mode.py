import time
battery_percentage=int(input("Enter the battery_percentage:"))
if battery_percentage<20:
    print("Activate Battery_saver_mode:")
if battery_percentage>20:
    print("Battery_percentage is sufficent no need  to on Battery_saver_mode:")
print()
time.sleep(2)
print("end of an application")

