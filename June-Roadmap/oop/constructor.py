## Step 2: __init__ method and Instance Variables
##problem with OUR previous approach:
# WE had to manually set attributes for each object after creation

## The __init__ method is a CONSTRUCTOR
# It runs automatically when we create an object

class Car:
    def __init__(self, owner, brand, model, year):
        """
        Constructor method - runs when object is created 'self' refers  to the object being created
        """
        #instance variables
        self.owner = owner 
        self.brand = brand 
        self.model = model 
        self.year = year
        print(f"SOLD TO {owner}! PRODUCT DETAILS: {brand} | {model} | {year} ")


car1 = Car("Gopal", "Toyota", "Camry", "2023")
print(car1.owner, car1.brand, car1.model, car1.year)

print("\n", "---" * 16)

class Person:
    def __init__(self, name, age, aim, hobby):
        #creating instance variables for Person class
        self.name = name
        self.age = age
        self.aim = aim
        self.hobby = hobby
    def person_info(self):
        print(f"Name: {self.name} Age: {self.age} Aim: {self.aim} Hobby: {self.hobby}")
person1 = Person("Gopal", 19, "Software Engineer", "Watching Football especially supporting Manchester City and sometime singing!")
person1.person_info()

print("\n", "---" * 16)

class Movie:
    def __init__(self, title, director, origin, lead_actors, is_superhit = bool):
        #instance variables
        self.title = title
        self.director = director
        self.origin = origin
        self.lead_actors = lead_actors
        self.is_superhit = is_superhit
        
    def movieDetails(self):
        print(f"Movie Name: {self.title} | Director: {self.director} | Origin: {self.origin} | Lead Actors: {self.lead_actors} | IS SUPERHIT: {self.is_superhit}")

m1 = Movie("Avengers Infinity War", "Russo Brothers", "HOLLYWOOD, US", "RDJ, Cris Hemsworth and Evens, Mark Rafello and others", is_superhit = True)
m1.movieDetails()

print("\n" + "---" * 16)

#creating a bank account class
class BankAccount:
    def __init__(self, name, initial_balance = 0, account_type = "Savings"):
        #instance variables
        self.name = name
        self.initial_balance  = initial_balance
        self.account_type = account_type
    def user_info(self):
        print(f"Account Holder: {self.name} | Initial Balance: {self.initial_balance}/- | Account Type: {self.account_type}")
user1 = BankAccount("Gopal", 4000)
user1.user_info()


#Creating a phone class 

print("\n" + "---" * 16)

class Phone:
    def __init__(self, brand, model, storage_gb, price):
        #instance variables
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.price = price
        
    def user_info(self):
        if self.storage_gb < 0 and self.price < 0:
            print("ENTER A VALID VALUE!")
        else:
            print(f"Brand: {self.brand} | Model: {self.model} | Storage: {self.storage_gb}GB | Price: {self.price}/-")

my_phone = Phone("MOTOROLA", "g35 5g", 128, 10000)
test1 = Phone("I don't have phone", " nothing ", - 1, - 1)
my_phone.user_info()
test1.user_info()



    
