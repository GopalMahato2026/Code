#what is inheritance?
"""
Inheritance lets you create a new class (child) that automatically gets the properties and methods of an existing class (parent).
"""
#parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speaks(self):
        return f"{self.name} is speaking!"

#child class
class Dog(Animal):
        pass

jony = Dog("JONNY")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
sim = Cat("Sim")
print(sim.speak())
print(jony.speaks())
print("---" * 16 )
"""
Create two classes:
Device (parent class) with attributes brand, price, and method info() that prints basic device info.
Smartphone (child class) that inherits from Device and adds an extra attribute camera_megapixel and method camera_info().
"""
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def deviceInfo(self):
        return f"Brand: {self.brand} | Price: {self.price}"

class Smartphone(Device):
    def __init__(self, brand, price ,camera_megapixel = None):
        super().__init__(brand, price)
        self.camera_megapixel = camera_megapixel
    
    def deviceInfo(self):
        baseInfo = super().deviceInfo() ## making my code DRY (Don't Repeat Yourself)
        return f"{baseInfo} | Camera Info: {self.camera_megapixel}"
    
p1 = Smartphone("MOTO G35 5G", 10000, "50 mp Back camera, 13 mp front camera")
print(p1.deviceInfo())





        
