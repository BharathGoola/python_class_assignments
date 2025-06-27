import time
current_hour=float(input("enter the time:"))
current_minute=int(input("enter the minutes:"))
if current_hour==5 and current_minute==30:
    print("Time is 5:00Am so, time to wake up:")
if current_hour!=5 or current_minute!=30:
    print("it's not 5:00Am:")
print()
time.sleep(2)
print("end of an application")
