#Required arguments--->it should match the exact number variables in calling with def
'''
a = 2
b = 6
def add (a,b):
    print(a+b)
add(a,b)
'''
#defalut arguments---->it will take the default values from the arguments
'''
name = "jai"
def add (name):
    print(name)
add(name = "sri")
add (name = "satya")

prime = int(input("Enter any number :"))
count = 0
def prim_check(prime,count_):
    for i in range(1,prime+1):
        if prime % i == 0:
           count_ += 1
    if count_ == 2:
       print(f"{prime} is a prime")
    else:
        print(f"{prime} is not a prime")
prim_check(prime,count)

def prim_check(prime,count):
    for i in range(1,prime+1):
        if prime % i == 0:
           count += 1
    if count == 2:
       print(f"{prime} is a prime")
    else:
        print(f"{prime} is not a prime")
prim_check(prime = 8,count = 0)
prim_check(prime = 7,count = 0)
prim_check(prime = 99,count = 0)


def num(apps,codes ,hats ):
    print(f" apps = {apps}, codes = {codes}, hats = {hats}")
num(hats = 8, codes = 10 ,apps = 7)
'''
#Variable length arguments---> adding a star(*) before the parammeter name in the function recieve a tuple of arguments and can access items with indexs
def items(*fruits):
    print(fruits[2])
items("apple","kiwi","banana")


