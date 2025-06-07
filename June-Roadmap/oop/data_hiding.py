"""
🔐 What is Data Hiding?
Data hiding means restricting direct access to some parts of an object — typically its internal data — so they can't be changed or misused accidentally.

⚙️ In Python:
We hide data using private attributes with __double_underscore.
But Python still allows access using a trick called name mangling.
"""

"""
🧪 Your Task — Practice:
Create a class PrivateDiary
Inside __init__, create a private attribute __entry = "Today I studied OOP in Python."
Add a method read_entry() to access it
Try to access __entry directly → then with name mangling
"""

class PrivateDiary:
    def __init__(self):
        self.__entry = "Today I studied OOP in Python"
    def read_entry(self):
        return self.__entry    

june7_1am = PrivateDiary()
print(june7_1am.read_entry())
"""
I only completed this in oop ✅ Step 11: Data Hiding – COMPLETED ✔️
You're now at 90% completion in your OOP Mastery Journey.
🔜 Final Stage:
Step 12: Complete Project using All OOP Concepts
This will include:
__init__, instance variables
Inheritance + super()
Method overriding + polymorphism
Abstract classes
Multiple inheritance
Encapsulation + data hiding
Getters and setters  



"""
