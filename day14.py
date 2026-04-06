#functions()
#--->this is a block of code which is reusable
#--->Two types 1.Built-in  or in-build  2.User defined 
'''
1.--->Built-in  or in-build
they comes with program and those are already defined....
eg-->print(),sum(),map()....
2.user_defined
-------
-->thi is created by person who is developing or using for development

#NOTE-->it starts with def keyword followed byy func name
--->And it has calling function....
                         |--------(parameters)
#SYNTAX--->def func-name(|):
           ----------
           ----------
           ----------
           func-name(|)
                     |------(arguments)

#EXAMPLE---->
def ev_odd(a=5):
    if a % 2 == 0:
       print(" is a even no")
    else:
        print(" is a odd no")
ev_odd(a=5)

user = int(input("enter any number :"))
def ev_odd(user):
    if user % 2 == 0:
       print(" is a even no")
    else:
        print(" is a odd no")
ev_odd(user)

prime = int(input("enter any number :"))
count = 0
def prime_check(prim,count):
    for j in range(1,prime+1):
        if prim % j == 0:
           count += 1
    if count == 2:
        print("prime")
    else:
            print("not prime")
prime_check(prime,count)
'''
palin = "madam"
empty=""
def pali_check(palin,empty):
    for j in palin:
        empty = j + empty
    if empty == palin:
        print("yes it is palin")
    else:
        print("no it not palin")
pali_check(palin,empty)

