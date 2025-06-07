# encapsulation in python
"""
What is Encapsulation?
Encapsulation is the concept of hiding internal object details from the out side world and only exposing what's necessary through methods
"""
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private attibute
        
    def deposite(self, amount): 
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}/-"
        return "Invalid Amount"
        
    
    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self, amount): #setter with control
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
            
acc = BankAccount("Gopal", 5000)
print(acc.get_balance())
print(acc.deposite(4000))
print(acc.get_balance())
#print(acc.__balance) will raise an error

print("---" * 16 )
# my turn
"""
🧪 Your Turn – Practice Task:
Create a class Student with:
Public: name
Private: __marks
Method set_marks(marks) → Only allows setting if 0 <= marks <= 100
Method get_marks() → Returns marks
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, mark):
        if mark <= 100 and mark >= 0:
            self.__marks = mark
        else:
            print("Invalid Mark!")

gopal = Student("Gopal", 78.82)
print(gopal.get_marks())
gopal.set_marks(82)
print(gopal.get_marks())

    
    
    
    


