
#Statements----->1.Conditional 2.control 3. loop
#if statement----- this (if satement) is used to check any condition ,
#..if the condition becomes true than it will enter into inside the (if statement).
'''

age = int(input("enter your age:"))
if age >= 20:
    print("your age is 20 above")
 
student_att = int(input("pls enter your sem attendence:"))
if  student_att >= 75:
    print("you can directly eligible to sit in the sem exam")

if elif statement
if-elif-else statement
coding questions

fee_details = int(input("pls enter your fee you cleared:"))
if  fee_details >= 28000:
    print("your are eligible to pay examination fee")

crt_training = int(input("pls enter your backlogs:"))
if  crt_training >= 2:
    print("your are not eligible to crt")
'''
# if elif statement---> this also called as fall back statement
#which only execute when the (if statement) becomes false
'''
age = int(input("enter your age:"))
if age >= 18:
    print("you can vote")
else:
    print(f"you cannot vote and have to wait { 18 - age} years")


total_amm = int(input("enter the total shopping money:"))
if total_amm >= 149:
    print("no delivery cost")
else:
    print(f"add {149 - total_amm} to your cart")
fee_amm = int(input("Enter the money you pay :"))
if fee_amm >= 40000:
    print("your access the codegnan JD")
else:
    print(f"your not eligible and you have to pay {40000 - fee_amm}")
'''
#if-elif-else statement(if + else)----> in the elif part, i can check one more condition
'''
student_marks = int(input("enter your marks:"))
if student_marks >= 90:
    print("you got A+ grade")
elif student_marks >= 75 and student_marks <= 90:
    print("you got A grade")
elif student_marks >= 60 and student_marks <= 75:
    print("you got B+ grade")
else:
    print(f"you are fail to pass  you get {90 - student_marks} marks
'''
#usinf if statements create----->calculator
'''
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
operand = input("enter the operand to perform the calculation:")
if operand == '+':
    print(num1 + num2)
elif  operand == '-':
    print(num1-num2)
elif operand == '*':
    print(num1*num2)
else :
    print(num1/num2)
'''
# using options----->calculator
'''
num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
user_choice = int(input("enter your choice \n1.ADD \n2.SUB \n3.mul \n4.div :"))
if user_choice == 1:
    print(num1+num2)
elif user_choice == 2:
    print(num1-num2)
elif user_choice == 3:
    print(num1*num2)
elif user_choice == 4:
    print(num1/num2)
'''
#even and odd
'''
user_choice = int(input("enter any number :"))
if user_choice % 2 == 0:
    print(f" {user_choice} is a even numnber")
else:
    print(f" {user_choice}  is odd number")
'''
#finding positive,negative or zero identifier
num = int(input("enter any number :"))
if num >0 :
       print("positive number")
elif num <0 :
    print("negative number")
else:
    print("the number is zero")
    

    
