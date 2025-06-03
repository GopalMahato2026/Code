class BankAccount:
    def __init__(self, account_holder, initial_balance=0, interest_rate=5, account_type="Saving"):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.transaction_history = []  # keep track of transactions

    def get_balance(self):
        # Returns the current balance
        return self.balance

    def calculate_interest(self, years=1):
        # Returns the interest earned after given years
        return (self.balance * self.interest_rate * years) / 100

    def deposit(self, amount):
        if amount <= 0:
            print("❌ INVALID AMOUNT! ENTER A VALID AMOUNT")
            return False
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}/-")
        print(f"✅ Deposited {amount}/-")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid Amount! Must be positive!")
            return False
        if amount > self.balance:
            print("❌ Insufficient Funds!")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn {amount}/-")
        print(f"✅ Successfully Withdrawn: {amount}/-")
        return True

    def transfer(self, other_account, amount):
        if self.withdraw(amount):  # if withdrawal successful
            other_account.deposit(amount)
            print(f"✅ Transferred {amount}/- to {other_account.account_holder}")
            return True
        return False

    def get_statement(self):
        print(f"\n📄 ACCOUNT STATEMENT for {self.account_holder}")
        print("-" * 50)
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}/-")
        print("Recent Transactions:")
        for transaction in self.transaction_history:
            print(f"  - {transaction}")
        print("-" * 50)

    def close_account(self):
        user = input("Do you really want to close the account? (y/n): ").lower()
        if user == 'y':
            self.balance = 0
            print("✅ Account closed.")
            return True
        print("❌ Account not closed.")
        return False


# Let's test this
gopal_account = BankAccount("Gopal", 1000, account_type="Checking")
arindam_account = BankAccount("Arindam", 500)

gopal_account.deposit(500)
print(f"Balance: {gopal_account.get_balance()}/-")
gopal_account.deposit(1000)
gopal_account.deposit(10000)
# gopal_account.withdraw(10000000)  # Uncomment to test insufficient funds
gopal_account.get_statement()
gopal_account.calculate_interest()
gopal_account.get_balance()


print("---" * 16)


## improved Phone class
class Phone:
    def __init__(self, brand, model, storage_gb, price):
        if storage_gb <= 0 and price <= 0:
            raise ValueError("Storage and Price must be positive")
        self.brand = brand 
        self.model = model
        self.storage_gb = storage_gb
        self.price = price
        self.app_installed = []
        self.photo_count = 0
    def install_app(self, app):
        if app not in self.app_installed:
            self.app_installed.append(app)
        if app in self.app_installed:
            print(f"{app} is already installed")
    def take_photo(self):   
        self.photo_count += 1
        print(f"PHOTO TAKEN! Total photos: {self.photo_count}")
     
    def get_storage_info(self):
        # calculating and displaying storage information
        used_storage = len(self.app_installed) * 0.5 + self.photo_count * 0.003 
        free_storage = self.storage_gb - used_storage
        print(f"Storage information for {self.brand} {self.model}")
        print(f"Total Storage: {self.storage_gb}GB")
        print(f"Used Storage: {used_storage}GB")
        print(f"Free Storage: {free_storage}")
        print(f"Apps: {len(self.app_installed)}, Total Photos: {self.photo_count}")
    def phone_info(self):
        print(f"\n {self.brand} {self.model}")
        print(f"Storage: {self.storage_gb}")
        print(f"Apps: {", ".join(self.app_installed) if self.app_installed else 'None'}")    

#Lets test
#(self, brand, model, storage_gb, price):

my_phone = Phone("Motorola", "g35 5G", 128, 10000)
my_phone.install_app("Udemy")
my_phone.install_app("Coding Python")
my_phone.take_photo()
my_phone.take_photo()
my_phone.take_photo()
my_phone.get_storage_info()
my_phone.phone_info()

print("---" * 16)

##Enhanced movie class
class Movie:
    def __init__(self, title, director, year, genre):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.ratings = []
        self.reviews = []
        self.times_watched = 0
    def add_ratings(self, rate):
        if 1 <= rate <= 10:
            self.ratings.append(rate)
        else:   
            print("Rating must be 1 to 10")

    def add_reviews(self, review):
        self.reviews.append(review)
        print(f"{review} adding Successfully!")


    def watch_movie(self):
        self.times_watched += 1
        print(f"Watching {self.title}, Watch count: {self.times_watched}") 

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def movie_summary(self):
        aver_rating = self.get_average_rating()
        print(f"\n {self.title} ({self.year})")
        print(f"Director: {self.director} Genre: {self.genre}")
        print(f"Average Rating: {aver_rating:.1f}")
        print(f"Times Watched: {self.times_watched} times!")
        if self.reviews:
            print("Recent reviews: ")
            for review in self.reviews:
                print("- \{review}\ ")
#lets test
interstaller = Movie("Interstaller" ,"Christopher Nolan", 2014, "Si-Fi")
interstaller.add_ratings(9)
interstaller.add_ratings(9)
interstaller.add_ratings(10)
interstaller.add_reviews("Currenty this is my best movie!")
interstaller.watch_movie()
interstaller.watch_movie()
interstaller.watch_movie()
interstaller.movie_summary()                


                       