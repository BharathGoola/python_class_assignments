import time
voted_members=["Bharath","Homeshwar","Satish","Ankit"]
voter=input("enter the name to vote:")
if voter in voted_members:
    print("the voter is already voted:")


if voter not in voted_members:
    print("thank you for voting:")
print()
time.sleep(2)
print("end of an application")
