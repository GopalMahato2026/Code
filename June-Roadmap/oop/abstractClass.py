## Abstract Classes & Interfaces
"""
What is an Abstract Class?
An abstract class is like a blueprint.
it can't be directly used to create objects, but other classes can inherit from it and must implement certain methods.
Why do we use it?
-To define a common structure for all child classes.
-To force child classes to implement some methods.
-Great for working with polymorphism in big projects.
"""
# python uses abc module:
from abc import ABC, abstractmethod
# So, ABC means abstract base class
# @abstractmethod means Marks a method that overridden in child classes
#abstract class
class Device(ABC):
    @abstractmethod
    def deviceInfo(self):
        pass

# child class

class Laptop(Device):
    def deviceInfo(self):
        return "My best friend is my LAPTOP! and my best partner!"
        
    
# another child class
class Phone(Device):
    def deviceInfo(self):
        return "My phone: Moto g35 5G" 

#d = Device() ERROR: Can't instantiate abstract class Device without an implementation for abstract method 'deviceInfo'
devices = [Laptop(), Phone()]
for device in devices:
    print(device.deviceInfo())

print("---" * 16)
"""
🧪 Your Turn: Practice Task
Create an abstract class Human with:
An abstract method occupation()
An abstract method goal()
*Then create 2 child classes:
Student → print "I'm studying to become a software engineer."
Teacher → print "I'm teaching students and guiding them."
"""
class Human(ABC):
    @abstractmethod
    def occupation(self):
        return "My father is a farmer!\n I think farmer is best occupation!\n Beacuse its give people what is the one of the most important thing for human being that is FOOD!"
    
    @abstractmethod
    def goal(self):
        return "making a better life for his sons!"
    # I made a mistake that is i write data in abstractmethods I think i sould keep this as it is
### child class
class Student(Human):
    def occupation(self):
        return "I'm studying to become a Software Engineer"
    def goal(self):
        return "Become Software Engineer in my 20th brithday"

## another child class
class Teacher(Human):   
    def occupation(self):   
        return "I'm teaching students and guiding them!"
    def goal(self):
        return "Making this world better by guiding students, Beacuse someday they will be the future!"

humans = [Student(), Teacher()]
for human in humans:
    print(human.occupation())
    print(human.goal())
    

        
    
