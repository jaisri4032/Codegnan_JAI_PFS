'''
tables = int(input("enter any number"))
for j in range(1,11):
    print(f"{tables} X {j} = {tables*j}")#printing tables
'''
#using string methods
'''
an = "Python IS Programming Language"
count_u = 0
count_l = 0
for char in an:
    if char.isupper():
        count_u += 1
    elif char.islower():
        count_l += 1
print(f"total capitals {count_u}")
print(f"total lowers {count_l}")

an = "Python IS Programming Language"
cap = []
small = []
for char in an:
    if char.isupper():
       cap.append(char)
    elif char.islower():
        small.append(char)
print(f"{cap} contain all caps")
print(f"{small} contain all small")#print caps and smalls

SBI_jai_details = {"name" : "jaisri",
                   "ATM_pin" : "0066"}
print("*****Welcome to SBI bank*****")
print("pls insert youre ATM card")
SBI_ATM_pin = input("Enter youre 4 digit ATM pin :")
if len(SBI_ATM_pin) == 4:
    if SBI_ATM_pin in SBI_jai_details['ATM_pin']:
        print("the pin is correct")
    else:
        print("you entered invalid ATM pin")
else:
    print("pls entered youre 4 digit ATM pin")
'''
per_num = int(input("Enter a number:"))
fact_all = 0
for i in range(1,per_num):
   if per_num % i == 0:
      fact_all += 1
if fact_all == per_num:
    print(f"{per_num} is a perfect number")
else:
    print(f"{per_num} is a not a perfect number")



    
 

