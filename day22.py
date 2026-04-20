
#Encapsulation:
    ----> the principle of bunding data(attributes) and methods that operate
    on that data into a single unit , which is a class

class bankAC:
    def __init__(self,balance):
       self.__balance = balance
    def deposite(self, amount):
        self.__balance += amount
    def get_bal(self):
        return self.__balance

acc = bankAC(20000)
acc.deposite(90)
print(acc.get_bal())

#Inheritance:
    ---> this allows a child class (sub class) to acquired the attributes and methods  of a
    parent class(bases class) called inheritance.
1.Singles inheritance
2.Multiple inheritance

1.Single inheritance--> using single method of the class from base class is know as single 
**super()
--->
to call methods parent class  from child class we use super() method.

class parent:
    def display(self):
        print("This is a parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is a child method")
obj = child()
obj.display()


2.Multiple inheritance: a child class inherit from more than one parent class.
'''
class father:
    def skill_1(self):
        print("father : hard working")
class mother:
    def skill_2(self):
        print("mother : queen of the home")
class child(father, mother):
    def all_skills(self):
        print("child: coding")
any = child()
any.skill_1()
any.skill_2()
any.all_skills()

           
    
       
