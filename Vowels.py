import time
str1=input("Enter the string object:") 
c=0
for x1 in str1:
    if(x1 in("AEIOUaeiou")):
        c+=1
        print("Vowels are:",x1)
print()
print("Number of vowels are:",c)
print()
time.sleep(2)
print("end of an application")
