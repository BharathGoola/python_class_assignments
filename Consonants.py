import time
str1=input("Enter the string_object:")
c1=0
for x1  in str1:
    if(x1 not in("AEIOUaeiou")):
         c1+=1
    print("Consonants are:",x1)
print()
print("Number of consonants:",c1)
print()
time.sleep(2)
print("end of an application")

