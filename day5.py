#STRING----> String is a sequence of characters/ collection of characters which represented by " " / ' '
'''

any = 'python programming'
print(any)
'''
#We can access the using 'indexing'
'''
any = "python programming"
print(any[7])
'''
#SLICING
#to print specific letter to specific letter we use slicing[1:1]
'''
any = "python programming"
print(any[7:13])

#example

any = "python programming"
print(any[7:16])
'''
#Mutable: list and immutable: tuple
'''
any = "python programming"
print(any.replace("python","GO"))
print(any)
'''
'''
any = "python programming"
so = (any.replace("python","GO"))
print(any)
print(so)
'''
#String can also negative indexing and also slicing
#it is immutable but where i could not able to modifyon the particular variable
'''
any = "python programming"
print(any[-2])
'''
#example using indexing slicing
'''
day_5 = ("this is jaisri from chodavaram,am python full stack trainee in codegnan today is day5")
print(f"my course is {day_5[-4:-1]}")
print(f" I am training {day_5[34:51]}")
print(f"my name is{day_5[9:15]}")
print(f"my name is{day_5[::-1]}")

a_day="Jaisri"
print(a_day[::-1])
'''

#len() --> len() method is used to get char present in the string or find the length of the string
'''
day_5 = ("this is jaisri from chodavaram,am python full stack trainee in codegnan today is day5")
print(len(day_5))
any="123"
print(len(any))

day_5="123"
num=int(day_5)
print(type(num))
'''
#note -- we can convert a strinng into integer, if the contain only integer values...
'''
some="123p"
num=int(day_5)
print(type(some))
'''
#Methods of String
#-----------------
#split()--> remove space, and the is in the list[] it will give the separated thing in each index 
#syntax --> Variable_name.split("substring")

#EXAMPLE
'''
some="python is a programming language"
print(some.split(""))#ValueError: empty separator
print(some.split(" "))
print(some.split("a"))
print(some.split("programming"))
'''

#lower()--> this is used to convert all letters into lowercase
#syntax --> Variable_name.lower()
'''
s="My Name Is Jaisri"
print(s.lower())
s=s.split(" ")
print(s)
'''
#upper()--> this is used to convert all letters into uppercase
#syntax --> Variable_name.upper()
'''
name = "my name is jaisri from chodavaram"
print(name.upper())
'''
'''
if "a" in name:
    print("yes it is there")
else:
    print("No,it is not there")
'''
#replace()----> this is used to replace ols str ro new str
#syntax---> variable_name.replace("old string","new string")
'''
name = "my name is jaisri from chodavaram"
print(name.replace("chodavaram","vizag"))

some = "pythom programming language"
if 'is' in some:
  print("yes")
else:
    print("no")



    

























