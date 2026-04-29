
import re
def validate_name(name):
    pattern=r'^[A-Za-z]{3,}$'
    return re.fullmatch(pattern,name)
def validate_email(email):
    pattern=r'[\w\.-]+@[\w\.-]*\-\*+$'
    return re.fullmatch(pattern,email)
def validate_phone(phone):
    pattern=r'^[0-9]{10}$'
    return re.fullmatch(pattern,phone)
def validate_password(password):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern,password)
def main():
    name=input("Enter Name:")
    email=input("Enter Email:")
    phone=input("Enter Phone Number:")
    password=input("Enter Password:")

    if not validate_name(name):
        print("Invalid name")
    elif not validate_email(email):
        print("Invalid email")
    elif not validate_phone(phone):
        print("Invalid phone number")
    elif not validate_password(password):
        print("Invalid Password")
    else:
        print("All inputs are valid! for submitted successfully")
if __name__== "__main__":
    main()

DATA ANALYSIS:
    Why this is need?
--------------------
-->This is critical becz it converts raw data into actionable
insights, enabling information to decision-making easy and improve operational efficiency...

1.Decision making
2.Improved operational efficiency
3.Customer understanding
4.Market Insights
5.Risk management
6.Data-Driven strategies
#Matplotlib---->line graph

import matplotlib.pyplot as pit
x = [1,2,3,4,5]
y = [10,20,15,26,10]
pit.plot(x,y)
pit.show()

#Bar graph

import matplotlib.pyplot as pit
pit.bar(["TV9","ZEETV","SumanTV"],[20,10,7])
pit.show()

import matplotlib.pyplot as pit
x = ["TV9","ZEETV","SumanTV"]
y = [20,10,7]
pit.bar(x,y)
pit.show()

#PIE:
import matplotlib.pyplot as pit
pit.pie([60,65,20,36], labels = ["jai","dhana","deepika","zai zai"])
pit.show()

#histogram:
import matplotlib.pyplot as pit
pit.hist([60,65,20,36])
pit.show()

#Numpy:

-->Numpy(Numerical python) is the foundational open-source library for scientific computing in python,
providing high-performance,N-dimensional
-->This enables efficient numerical computation linear algebra, and data manipulation,serving as the
basis like TensorFlow and Scipy

import numpy as np
arr = np.array([1,2,3])
print(arr)

import numpy as np
arr = np.array([1,2,3])
print(arr-1)


#Pandas:
-->used for  handling structured data in table formate

import pandas as pd
data = {"Name" : ["Jai","Dhanu"], "Marks": [90,89]}
any = pd.DataFrame(data)
print(any)






