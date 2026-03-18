'''
Variables --> variable is basically named storage location that is used to store
data in te memory , to make it simple it is the label which points
out to a vale -->storage placeholders

Rules for defining variables
-->A-Z,a-z.0-9
-->start with uppercase,lowercase letters ,even with a underscore_
-->But you cannot start with symbols (@,#,$....),even numbers also

Better preferable way is go with general purpose -->you want to store
your details name,email_id,account_number..

'''
'''
a=2
b=300
a=25
#python is dynamically typed,you need not define the datatype and also
#only the recent value to the variable with same name is pointed

print(b)
print(a)

#1b23 = 25 #syntax error
#@ert = 4.5 #syntax error

#Store the personal details
name = "codegnan"
location = "visakhapatnam"
age = 7
email_id = "vmc@codegnan.com"
print(name,age,location,email_id)

#how to assign multiple values to a variables
jai,gowri,sai = 21,20,21
print(jai)
print(sai)
print(gowri)

#assig  the same values to the multiple variables
jai = sai = gowri = 19
print(jai,sai,gowri)

#keywords are reserved words will have specific usage
#there are 35 keyword in python
#never use  keywords as identifiers

#if = 30
#lambda = 'jai'
#False = 0#can't assign

#python is case sensitive
false = 5

#identifiers are names is given to functions, classes and objects......

#Literals are fixed values to a Identifier
name = 25

#name is Idetifier,25 is literal

#Single line comments ---> #
#Multi line comments ---> start end with triple quotes

#Built-in Datatypes -->Numeric,Boolean,Collections

#Numeric datatypes --> int ,float,complex
#int -->count,values,quantites
#float --> temperature,percentage,price
#specific --> specific conversions (real and imaginary number)
'''
'''
count = 40
print(count)
print(type(count))

price = 1.45
print(price)
print(type(price))

count = 40
print(40)
print(type(count))

'''
'''
j3 = 25
value = 2+j3
print(value)
print(type(value))
'''
#type casting---> converting one type to another type
 #int-->float,complex
'''
age = 25
print(type(age))
print(age)
b = float(age)
print(type(b))
print(b)
c = complex(age)
print(type(age))
print(c)
'''
'''
#float,complex
price = 275.25
print(type(price))
d = int(price)
print(type(d))
'''
#complex to int is not possible
#complex to float is not possible

#boolean datatype -->validation -->True / False
''''
a = True
print(a)
print(type(a))

#tupeconversion of bool

b = int(a)
print(b)
c = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))
'''

#Input --> input()/ output--->print()
'''
a = 5
print(a)

a = input("enter the value")#any input but result is str
print(a)
print(type(a))


a = int(input("enter the value:"))# only integer input
print(a)
print(type(a))

a = float(input("enter the value:"))#only float input
print(a)
print(type(a))
'''

#Now let's work on a simple case study using above -->Fee calculator

#details of student
name = input("Enter the student name:")
print("------------")
admission_fee = int(input("Enter the Admission Fee:"))
tuition_fee = float(input("Enter the Tuition Fee:"))
hostel_fee = float(input("Enter the Hostel Fee"))
# calculte the total fee
total_fees = admission_fee +tuition_fee + hostel_fee                  
print("<------------------------>")
print("Student name :",name)
print("Admission fee :",admission_fee)
print("Tuition fee :",tuition_fee)
print("Hostel fee :",hostel_fee)
print("Total fees :",total_fees)
print("<------------->)






































