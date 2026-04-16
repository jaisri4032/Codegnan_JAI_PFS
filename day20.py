'''
-->00P'S object oriented programming is a style of programming where we model real-world
   thing as object that contains both data and functions()
>>>WHY:
   *reusable of code
   *Scalable

>>CLASS:
-->class is blueprint or template that defines what kind of data
   and behaviour of certain type of object will have
>>>SYNTAX:
   **class class_Name:
      pass
>>>EXAMPLE:
   **class bike:
         pass
--------------------------------------------------------------------------
>>>OBJECT:
-->Instance of class or an object is a real instance created from class.
   it is actutal thing that exists in memory while program runs

class car:
    pass
car1 = car()#objects
car2 = car()#objects
-----------------------------------------------------------------------------
>>>ATTRIBUTES:
--> these are the variables that store data realated to class or objects

class dog:
    def __init__(self,breed,color):
       self.breed = breed
       self.color = color         
dog_1 = dog("bull dog","white/cream")
dog_2 = dog("labrador", "black")
print(dog_2.breed)
'''
class car:
    wheels = 4
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 20
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} Miles. Total: {self.mileage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"
car1 = car(make="ford", model="mustang", year="2008")
car2 = car(make="toyota", model="camry", year="2023")
print(car1.info())
print(car2.info())
print(car2.drive(10))












