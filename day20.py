#Modules-->A module  in a python os simply file that contains python code(functions,varaibles,classes)
#To use modules,we have to use keyword called import before the module.
'''
TYPES-->1.Bulit-in or inbuilt  2. User_define modules

--->**User defined module--->this ia developed by user or programmer inside a file  of python code and
      used by called import with filename.
SYNTAX:
      import(keyword) file_name
      file_name.functionality

EXAMPLE:

import module
print(module.add(10,20))

import day5
print(day5.han(any))                                      

**Built_in or inbuilt--->Already these are comes with installation and they are ready to use in the program.
--->this is developed by developers..

import math
print(math.sqrt(36))
'''
import random
attempts = 3
while attempts > 0:
    user = int(input())
    tar = random.randint(1,90)
    print(tar)
    if  user == tar:
        print("you win")
    else:
        attempts -= 1
if attempts == 0:
   print("you lose")
   
