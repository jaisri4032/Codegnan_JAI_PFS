
#Multi-level inheritance:
'''
    This occurs when a class inherits from a child class ,
    creating  a grandparent --> parent --> child in this structure.
'''
class grandparent:
    def show_grandparent(self,name):
        self.name = name
        print(f"Iam grandparent {self.name}")
class parent(grandparent):
    def show_parent(self):
        print("Iam parent")
class child(parent):
    def show_child(self):
        print("Iam child")
any = child()
any.show_grandparent("jayamma")
any.show_parent()
any.show_child()

class Vehicle:
    def info(self):
        print("This is a land vehicle.")
class Car(Vehicle):
    def drive(self):
        print("The car is driving on four wheels.")
class ElectricCar(Car):
    def charge(self):
        print("The electric car is charging its battery.")
my_tesla = ElectricCar()
my_tesla.info()    
my_tesla.drive()   
my_tesla.charge()

#Hierchical:
----> this occurs when multiple child classes inherit from a single parent
      class, this process is called Hierchical.
      
class parent:
    def parent(self):
        print("Im a parent")
class child_1(parent):
    def child_(self):
        print("im 1st child")
class child_2(parent):
    def _child(self):
        print("im 2nd child")
class child_3(child_1, child_2):
    def child(self):
        print("im  child")
thing = child_3()
thing.parent()
thing.child_()
thing._child()
thing.child()


#Hybrid inheritance:
---->This is a combination of two or more types of inheritance such as single, multiple, multi level, or
hierchical, all this in a single class.
'''
class grandparent:
    def show_grandparent(self):
        print("Iam grandparent ")
class parent(grandparent):
    def show_parent(self):
        print("Iam parent")
class child(parent):
    def show_child(self):
        print("Iam child")
class parent:
    def parent(self):
        print("Im a parent")
class child_1(parent):
    def child_(self):
        print("im 1st child")
class child_2(parent):
    def _child(self):
        print("im 2nd child")
class child_3(child_1, child_2,grandparent):
    def child(self):
        print("im  newly inherited child")
thing = child_3()
thing.show_grandparent()
thing.parent()
thing.child_()
thing._child()
thing.child()



    
    
    
