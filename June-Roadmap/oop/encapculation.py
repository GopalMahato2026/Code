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
            return f"Deposited: {amount}/-
        return "Invalid Amount"
        
    
    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self, amount): #setter with control
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")
            
acc = BankAccount("Gopal", 5000)
acc.get_balance()
    
    
    
    


