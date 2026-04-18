'''
Constructor--->
A constructor is special method used to initialize object data
__init__()

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
'''
class trainee:
    
    def __init__(self):
        self.name = "name"
        self.course = "course"
        self.year = "year"
    def display(self):
        print(self.name,self.course, self.year)
trai_1 = trainee(name="jai", course="PFS", year="2026")
trai_2 = trainee(name="kavya", course="PFS", year="2026")
trai_1.display()
print(trai_2.display())

'''
Access specifiers:
------->1.Public
        2.protected
        3.private
1.--->PUBLIC:
SYNTAX:-->  name
we can use it anywhere in the program
---->2.PROTECTED:
SYNTAX:-->  _name
this is only for iternal use
---->PRIVATE:
SYNTAX:-->  __name
this one is restricted

class bank:
    
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"
any = bank()
print(any.public)
print(any._protected)
print(any.__private)

--->SELF:
    this keyword is instance variable and unique for each object

'''




