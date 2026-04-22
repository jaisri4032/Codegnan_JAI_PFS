'''
#Polymorphism:

    this allows the object of different classes to be treated as instance
    of the same base class , with methods behaving different based on the actual object type.
#EXAMPLE:

print(len("python"))
print(len([1,2,3]))

#Method overloading:
This defines multiple methods with the same name but different parameters
(number, type, or order) in same class.
'''
#EXAMPLE:
'''
class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
cal = calculator()
print(cal.add(2))
print(cal.add(10,3))
print(cal.add(200,700,300))


class calculator:
    def add(self, a, b, c=1):
        return a*b*c
cal = calculator()
print(cal.add(2,7))
print(cal.add(10,3))
print(cal.add(200,700,300))

#Method overriding:
this occurs in the child class,redefining a parent class method with
same signature for runtime.
#EXAMPLE:



class animal:
    def speak(self):
        return "sound"
class dog(animal):
    def speak(self):
        return "bow bow"
dog_ = dog()
print(dog_.speak())

#import sound to speech:

import pyttsx3
engine = pyttsx3.init()

class animal:
    def speak(self):
        return "sound"

class dog(animal):
    def speak(self):
        return "muskoni undu ra pula chokka"
dog_ = dog()
speech_text = dog_.speak()
print(speech_text)
engine.say(speech_text)
engine.runAndWait()


operator overloading:
    this is customizes operator like +, - for userdefined classes by
    implementing special methods.
eg..__add__, __sub__

#EXAMPLE:

class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return someone(self.a +other.a, self.b +other.b)
    def __str__(self):
        return f"[{self.a}, {self.b}]"
any = someone(2,3)
so = someone(5,9)
print(any + so)


Data abstraction:
    this hides complex implememtation details, exposing only essential
    features via abstract class or interface.
    '''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
Circle = circle(4)
print(Circle.area())
