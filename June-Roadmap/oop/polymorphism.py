# What is Polymorphism?
"""
Polymorphism means many forms.
in OOP, different classes can have methods with same name, but their behavior is different.

in my previous inheritance program i call a method like .deviceInfo(), it will act differently dependaing on the object's class 
even if the method name is the same.
"""
#example 1: Same method name, Different class
"""
class Laptop:
    def deviceInfo(self):
        return "Laptop: LENOVO, My One Only Love"

class Phone:
    def deviceInfo(self):
        return "My Phone: Moto G35 5G"
#polymorphism in action
devices = [ Laptop(), Phone()]

for d in devices:
    print(d.deviceInfo())
""" 
"""
## polymorphism via inheritance
class Device:
    def deviceInfo(self):
        return "Generic device"
class Tablet(Device):
    def deviceInfo(self):
        return "Tablet Samsung"
class SmartWatch(Device):   
    def deviceInfo(self):
        return "smart watch: budget one 999"

# polymorphism with inheritance classes
gedgets = [Device(), Tablet(), SmartWatch()]
for g in gedgets:
    print(g.deviceInfo())
"""        
print("---" * 16)
"""
practice task for me 
Create 3 classes:
Device (parent)
Laptop, Smartphone (child classes)
Each should have a method deviceInfo() that returns a unique string.
"""
class Devices:
    def deviceInfo(self):
        return "This is a generic device"
class Laptop(Devices):
    def deviceInfo(self):
        return "My laptop: This is my Love This will help me to get a Software Engineer Job"
class Smartphone(Devices):
    def deviceInfo(self):
        return "My smartphone details: Moto g35 5G "
class Ai(Devices):
    # just for practice
    def deviceInfo(self):
        return "Chat Gpt Helps me a lot!, He show me direction to archive my Aim"
        
    
mates =    [Devices(), Laptop(), Smartphone(), Ai()] 
for mate in mates:
    print(mate.deviceInfo())
        
