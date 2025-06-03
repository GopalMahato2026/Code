### What is class ?
"""
A class is a blueprint or template for creating objects
Think of it like a cookie cutter - it defines the shape,  but each cookie (object) is unique
"""
# Basic class definition
class Car:
    pass #empty class for now

#creating objects (Instances)
my_car = Car()
your_car = Car()

print(f"my_car is of type: {type(my_car)}")
print(f"your_car is of type: {type(your_car)}")
print(f"Are they the same object? {my_car is your_car}")

#adding attributes to the objects
my_car.brand = "Toyota"
my_car.model = "Camry"
my_car.year = 2023

your_car.brand = "Honda"
your_car.model = "Civic"
your_car.year = 2022

print(f"My car: {my_car.brand} {my_car.model} {my_car.year}")
print(f"Your car: {your_car.brand} {your_car.model} {your_car.year}")
### exercise 1: Creating my first class
print("\n" + "--"*25)
print("EXERCISE 1: Creating a Person class")
print("\n" + "--"*25)

class Person: ## class name always capital
    pass
    
#creating two person object
person1 = Person()
person2 = Person()
person3 = Person()
##adding attributes
person1.name = "Gopal"
person2.name = "Arindam"
person3.name = "Yubraj"

person1.age = "19"
person2.age = "18"
person3.age = "21"

person1.balance = 25.00
person2.balance = 50.00
person3.balance = 0.00

print(f"Person 1: {person1.name} | {person1.age} | {person1.balance}")
print(f"Person 2: {person2.name} | {person2.age} |  {person2.balance}")
print(f"Person 3: {person3.name} | {person3.age} |  {person3.balance}")
print("\n" + "--"*25)
#exercise 2: Creating a book class
print("\n" + "--"*25)

class Book:
    pass

my_book1 = Book()
my_book2 = Book()

my_book1.name = "Think and Grow Rich"
my_book1.price = 180
my_book1.auther = "Nepoleon Hill"
my_book1.is_finished = False

my_book2.name = "AI a new systhesic"
my_book2.price = "College Property"
my_book2.auther = "I didn't see yet!"
my_book2.is_finished = False

print(f"Book 1: {my_book1.name} | {my_book1.price}/- | {my_book1.auther} | {my_book1.is_finished}")
print(f"Book 2: {my_book2.name} | {my_book2.price}/- | {my_book2.auther} | {my_book2.is_finished}")

print("\n" + "--" * 25)
# exercise 3: creating a movie class and also creating instances with attributes like title, director, year, rating

class Movie:
    pass

top1_movie = Movie()
top2_movie = Movie()

top1_movie.title = "Interstellar"
top1_movie.director = "Cristopher Nolan"
top1_movie.year = 2014

top2_movie.title = "Avengers Infinity War"
top2_movie.director = "Russo Brothers"
top2_movie.year = 2018
print(f"Top 1 movie: {top1_movie.title} | {top1_movie.director} | {top1_movie.year}")
print(f"Top 2 movie: {top2_movie.title} | {top2_movie.director} | {top2_movie.year}")

## trying printing attributes that are not wrote
#print({top1_movie.boxoffice}) ## seeing attribute error





    
