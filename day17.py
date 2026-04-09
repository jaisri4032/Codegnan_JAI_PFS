#Lambda function
'''
---------------
-->This is also called as anonymous function.
-->A lamda function can take n number of arguments but have only one expression
'''
#SYNTAX:
#    lambda(keyword) arguments : expression
'''
sum = lambda add : add + 10# for one argument
print(sum(1))

sum = lambda add,add_2 : add_2add + 10#for multiple arguments
print(sum(1,3))

sum = lambda add,add_2 : (add_2+add) * 10
print(sum(1,3))

sum = lambda sub,sub_2,mul : (sub_2-sub) * mul
print(sum(1,3,2))

div = lambda app,bag : app / bag
print(int(div(15,3)))

mul = lambda code,data : code * data
print(int(mul(15,3)))
'''
#List comprehension:
'''
-------------------
-->This offers the shorter syntax when you want to create a new list from existing list
'''
#SYNTAX:
#        Variable_name = {expression loop and conditon}
'''
list_1 = [6,7,8,9,0]
list_2 = [ sto for sto in list_1]
print(list_2)

list_1 = [6,7,8,9,0]
list_2 = [ sto for sto in list_1 if sto%2==0]#even
print(list_2)
'''
list_1 = [6,7,8,9,0]
list_2 = [ sto for sto in list_1 if sto%2!=0]#odd
print(len(list_2))#for length
