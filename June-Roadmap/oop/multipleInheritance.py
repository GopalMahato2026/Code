# Multiple inheritances in python
"""
What is Multiple Inheritance?
In Python, a class can inherit from more that one parent class. This is called multiple Inheritance.
"""
# this is the basic syntax:
"""
class ChildClass(Parent1, Parent2):
    # inherits all methods and variables from both
    pass
"""
# creating a class combine feature of camera and phone 
class Camera:
    def take_photo(self):
        return "Photo taken at 1080p resolution"
class Phone:    
    def make_call(self):    
        return "Calling using Sim"

#multiple Inheritance

class Smartphone(Camera, Phone):
    def deviceInfo(self):
        return "This is a smartphone"


d = Smartphone()
print(d.deviceInfo())
print(d.take_photo())
print(d.deviceInfo())
print("----" * 16)

# my turn practice set
"""
🧪 Your Turn — Practice Task:
Create these 3 classes:
Writer: method write() → "I write stories and articles."
Singer: method sing() → "I sing songs with emotion."
Artist: inherit from both, and method intro() → "I am a creative artist."
"""
#parent class 1
class Writer:
    def write(self):
        return "I write stories and articles poem observation things"

#parent class 2
class Singer:   
    def sing(self):
        return "I sing songs with emotions"

## now this class will inherit from both parent class 1 and parent class 2

class Artist(Writer, Singer):
    def intro(self):
        return "I'm a creative artist"

aFamousArtist = Artist()
print(aFamousArtist.intro())
print(aFamousArtist.write())
print(aFamousArtist.sing())


        





