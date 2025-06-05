import datetime
import json
import uuid
from typing import List, Dict, Optional
from enum import Enum

print("🏦 COMPLETE BANK ACCOUNT PRACTICE PROJECT")
print("=" * 60)

class AccountType(Enum):
    SAVINGS = "Savings"
    CHECKING = "Checking"
    PREMIUM = "Premium"
    STUDENT = "Student"
    BUSINESS = "Business"

class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAWAL = "Withdrawal"
    TRANSFER = "Transfer"
    INTEREST = "Interest"
    FEE = "Fee"
    REFUND = "Refund"

class Transaction:
    def __init__(self, transaction_type: TransactionType, amount: float, 
                 description: str, balance_after: float):
        self.id = str(uuid.uuid4())[:8]
        self.type = transaction_type
        self.amount = amount
        self.description = description
        self.balance_after = balance_after
        self.timestamp = datetime.datetime.now()
    
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} | {self.type.value} | ₹{self.amount} | {self.description} | Balance: ₹{self.balance_after}"

class BankAccount:
    # Class variables
    total_accounts = 0
    bank_name = "PyBank"
    
    def __init__(self, account_holder: str, initial_balance: float = 0, 
                 account_type: AccountType = AccountType.SAVINGS, 
                 interest_rate: float = 0.02, min_balance: float = 100):
        
        # Input validation
        self._validate_inputs(account_holder, initial_balance, interest_rate)
        
        # Generate unique account number
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{BankAccount.total_accounts:06d}"
        
        # Basic account information
        self.account_holder = account_holder.strip()
        self.balance = initial_balance
        self.account_type = account_type
        self.interest_rate = interest_rate
        self.min_balance = min_balance
        self.account_active = True
        self.created_date = datetime.datetime.now()
        
        # Advanced features
        self.transactions: List[Transaction] = []
        self.overdraft_limit = 0
        self.monthly_transaction_limit = 50
        self.daily_withdrawal_limit = 10000
        self.daily_withdrawals = 0
        self.last_withdrawal_date = None
        self.freeze_status = False
        self.pin = None
        self.failed_pin_attempts = 0
        self.max_pin_attempts = 3
        
        # Set account-specific limits based on type
        self._set_account_limits()
        
        # Create initial transaction
        if initial_balance > 0:
            self._add_transaction(TransactionType.DEPOSIT, initial_balance, 
                                f"Account opened with initial balance")
        
        print(f"✅ {self.account_type.value} account created successfully!")
        print(f"   Account Number: {self.account_number}")
        print(f"   Holder: {self.account_holder}")
        print(f"   Initial Balance: ₹{self.balance}")
        print(f"   Interest Rate: {self.interest_rate*100}%")
    
    def _validate_inputs(self, account_holder: str, initial_balance: float, interest_rate: float):
        if not account_holder or len(account_holder.strip()) == 0:
            raise ValueError("Account holder name cannot be empty!")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative!")
        if interest_rate < 0 or interest_rate > 1:
            raise ValueError("Interest rate must be between 0 and 1!")
    
    def _set_account_limits(self):
        limits = {
            AccountType.SAVINGS: {'min_balance': 100, 'daily_limit': 5000, 'overdraft': 0},
            AccountType.CHECKING: {'min_balance': 50, 'daily_limit': 10000, 'overdraft': 1000},
            AccountType.PREMIUM: {'min_balance': 500, 'daily_limit': 50000, 'overdraft': 5000},
            AccountType.STUDENT: {'min_balance': 0, 'daily_limit': 3000, 'overdraft': 0},
            AccountType.BUSINESS: {'min_balance': 1000, 'daily_limit': 100000, 'overdraft': 10000}
        }
        
        account_limits = limits[self.account_type]
        self.min_balance = account_limits['min_balance']
        self.daily_withdrawal_limit = account_limits['daily_limit']
        self.overdraft_limit = account_limits['overdraft']
    
    def _add_transaction(self, trans_type: TransactionType, amount: float, description: str):
        transaction = Transaction(trans_type, amount, description, self.balance)
        self.transactions.append(transaction)
    
    def _reset_daily_withdrawals(self):
        today = datetime.date.today()
        if self.last_withdrawal_date != today:
            self.daily_withdrawals = 0
            self.last_withdrawal_date = today
    
    def set_pin(self, pin: str) -> bool:
        if len(pin) != 4 or not pin.isdigit():
            print("❌ PIN must be exactly 4 digits!")
            return False
        self.pin = pin
        print("✅ PIN set successfully!")
        return True
    
    def verify_pin(self, pin: str) -> bool:
        if self.pin is None:
            print("⚠️ No PIN set for this account!")
            return True
        
        if self.failed_pin_attempts >= self.max_pin_attempts:
            print("🔒 Account locked due to too many failed PIN attempts!")
            self.freeze_account()
            return False
        
        if pin == self.pin:
            self.failed_pin_attempts = 0
            return True
        else:
            self.failed_pin_attempts += 1
            remaining = self.max_pin_attempts - self.failed_pin_attempts
            print(f"❌ Incorrect PIN! {remaining} attempts remaining.")
            return False
    
    def freeze_account(self):
        self.freeze_status = True
        print("🧊 Account has been frozen!")
    
    def unfreeze_account(self, admin_code: str = "ADMIN123"):
        if admin_code == "ADMIN123":
            self.freeze_status = False
            self.failed_pin_attempts = 0
            print("🔓 Account has been unfrozen!")
            return True
        else:
            print("❌ Invalid admin code!")
            return False
    
    def deposit(self, amount: float, pin: str = None) -> bool:
        if not self._can_perform_transaction(pin):
            return False
        
        if amount <= 0:
            print("❌ Deposit amount must be positive!")
            return False
        
        self.balance += amount
        self._add_transaction(TransactionType.DEPOSIT, amount, f"Cash deposit")
        print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.balance}")
        return True
    
    def withdraw(self, amount: float, pin: str = None) -> tuple[bool, float]:
        if not self._can_perform_transaction(pin):
            return False, self.balance
        
        if amount <= 0:
            print("❌ Withdrawal amount must be positive!")
            return False, self.balance
        
        self._reset_daily_withdrawals()
        
        if self.daily_withdrawals + amount > self.daily_withdrawal_limit:
            print(f"❌ Daily withdrawal limit exceeded! Limit: ₹{self.daily_withdrawal_limit}")
            return False, self.balance
        
        available_balance = self.balance + self.overdraft_limit
        if amount > available_balance:
            print(f"❌ Insufficient funds! Available: ₹{available_balance}")
            return False, self.balance
        
        if (self.balance - amount) < -self.overdraft_limit:
            print(f"❌ Would exceed overdraft limit of ₹{self.overdraft_limit}")
            return False, self.balance
        
        self.balance -= amount
        self.daily_withdrawals += amount
        
        if self.balance < 0:
            fee = abs(self.balance) * 0.02  # 2% overdraft fee
            self.balance -= fee
            self._add_transaction(TransactionType.FEE, fee, "Overdraft fee")
            print(f"⚠️ Overdraft fee of ₹{fee} applied")
        
        self._add_transaction(TransactionType.WITHDRAWAL, amount, f"Cash withdrawal")
        print(f"✅ Withdrew ₹{amount}. New Balance: ₹{self.balance}")
        return True, self.balance
    
    def transfer(self, recipient_account: 'BankAccount', amount: float, 
                pin: str = None, description: str = "Transfer") -> bool:
        if not self._can_perform_transaction(pin):
            return False
        
        if amount <= 0:
            print("❌ Transfer amount must be positive!")
            return False
        
        if not recipient_account.account_active:
            print("❌ Recipient account is not active!")
            return False
        
        # Withdraw from sender
        success, _ = self.withdraw(amount, pin)
        if not success:
            return False
        
        # Deposit to recipient
        recipient_account.balance += amount
        recipient_account._add_transaction(TransactionType.TRANSFER, amount, 
                                         f"Transfer from {self.account_number}: {description}")
        
        # Update sender's transaction
        self._add_transaction(TransactionType.TRANSFER, -amount, 
                            f"Transfer to {recipient_account.account_number}: {description}")
        
        print(f"✅ Transferred ₹{amount} to {recipient_account.account_holder}")
        return True
    
    def apply_interest(self, years: float = 1) -> float:
        if not self.account_active or self.balance <= 0:
            print("❌ Cannot apply interest!")
            return self.balance
        
        interest = self.calculate_interest(years)
        old_balance = self.balance
        self.balance += interest
        
        self._add_transaction(TransactionType.INTEREST, interest, 
                            f"Interest applied for {years} year(s)")
        
        print(f"💰 Interest Applied: ₹{interest}")
        print(f"   Old Balance: ₹{old_balance} → New Balance: ₹{self.balance}")
        return self.balance
    
    def calculate_interest(self, years: float = 1) -> float:
        if years <= 0 or self.balance <= 0:
            return 0
        return round(self.balance * self.interest_rate * years, 2)
    
    def _can_perform_transaction(self, pin: str = None) -> bool:
        if not self.account_active:
            print("❌ Account is closed!")
            return False
        
        if self.freeze_status:
            print("🧊 Account is frozen!")
            return False
        
        if self.pin and not self.verify_pin(pin):
            return False
        
        return True
    
    def close_account(self, pin: str = None) -> bool:
        if not self.verify_pin(pin):
            return False
        
        if self.balance < 0:
            print(f"❌ Cannot close account with negative balance: ₹{self.balance}")
            return False
        
        self.account_active = False
        print(f"🔒 Account {self.account_number} has been closed.")
        print(f"   Final balance: ₹{self.balance}")
        return True
    
    def get_balance(self) -> float:
        return self.balance
    
    def get_account_info(self) -> Dict:
        return {
            "account_number": self.account_number,
            "holder": self.account_holder,
            "balance": self.balance,
            "type": self.account_type.value,
            "interest_rate": f"{self.interest_rate*100}%",
            "min_balance": self.min_balance,
            "overdraft_limit": self.overdraft_limit,
            "daily_limit": self.daily_withdrawal_limit,
            "active": self.account_active,
            "frozen": self.freeze_status,
            "created": self.created_date.strftime("%Y-%m-%d"),
            "total_transactions": len(self.transactions),
            "has_pin": self.pin is not None
        }
    
    def get_transaction_history(self, limit: int = 10) -> List[Transaction]:
        return self.transactions[-limit:] if limit > 0 else self.transactions
    
    def get_monthly_statement(self, month: int = None, year: int = None) -> Dict:
        if not month:
            month = datetime.datetime.now().month
        if not year:
            year = datetime.datetime.now().year
        
        monthly_transactions = [
            t for t in self.transactions 
            if t.timestamp.month == month and t.timestamp.year == year
        ]
        
        total_deposits = sum(t.amount for t in monthly_transactions if t.type == TransactionType.DEPOSIT)
        total_withdrawals = sum(t.amount for t in monthly_transactions if t.type == TransactionType.WITHDRAWAL)
        total_fees = sum(t.amount for t in monthly_transactions if t.type == TransactionType.FEE)
        
        return {
            "month": f"{month}/{year}",
            "total_transactions": len(monthly_transactions),
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "total_fees": total_fees,
            "net_change": total_deposits - total_withdrawals - total_fees,
            "transactions": monthly_transactions
        }
    
    def export_data(self) -> str:
        """Export account data as JSON"""
        data = {
            "account_info": self.get_account_info(),
            "transactions": [
                {
                    "id": t.id,
                    "type": t.type.value,
                    "amount": t.amount,
                    "description": t.description,
                    "balance_after": t.balance_after,
                    "timestamp": t.timestamp.isoformat()
                }
                for t in self.transactions
            ]
        }
        return json.dumps(data, indent=2)
    
    @classmethod
    def get_bank_stats(cls) -> Dict:
        return {
            "bank_name": cls.bank_name,
            "total_accounts_created": cls.total_accounts
        }
    
    def __str__(self):
        return f"BankAccount({self.account_number}, {self.account_holder}, ₹{self.balance})"

# Demo and Testing
print("\n🧪 COMPREHENSIVE TESTING")
print("=" * 60)

try:
    # Create different types of accounts
    print("\n1️⃣ Creating Multiple Account Types...")
    savings_acc = BankAccount("Alice Johnson", 5000, AccountType.SAVINGS, 0.03)
    checking_acc = BankAccount("Bob Smith", 2000, AccountType.CHECKING, 0.01)
    premium_acc = BankAccount("Carol Wilson", 10000, AccountType.PREMIUM, 0.05)
    
    # Set PINs
    print("\n2️⃣ Setting up PINs...")
    savings_acc.set_pin("1234")
    checking_acc.set_pin("5678")
    premium_acc.set_pin("9999")
    
    # Test transactions
    print("\n3️⃣ Testing Transactions...")
    savings_acc.deposit(1000, "1234")
    checking_acc.withdraw(500, "5678")
    
    # Test transfer
    print("\n4️⃣ Testing Transfer...")
    premium_acc.transfer(savings_acc, 2000, "9999", "Birthday gift")
    
    # Test interest
    print("\n5️⃣ Applying Interest...")
    savings_acc.apply_interest()
    
    # Display account information
    print("\n6️⃣ Account Information...")
    for account in [savings_acc, checking_acc, premium_acc]:
        print(f"\n📋 {account.account_holder}'s Account:")
        info = account.get_account_info()
        for key, value in info.items():
            print(f"   {key}: {value}")
    
    # Show recent transactions
    print("\n7️⃣ Recent Transactions...")
    for account in [savings_acc, checking_acc, premium_acc]:
        print(f"\n📊 {account.account_holder}'s Recent Transactions:")
        recent = account.get_transaction_history(3)
        for transaction in recent:
            print(f"   {transaction}")
    
    # Monthly statement
    print("\n8️⃣ Monthly Statement Example...")
    statement = premium_acc.get_monthly_statement()
    print(f"Statement for {statement['month']}:")
    print(f"   Total Transactions: {statement['total_transactions']}")
    print(f"   Total Deposits: ₹{statement['total_deposits']}")
    print(f"   Total Withdrawals: ₹{statement['total_withdrawals']}")
    print(f"   Net Change: ₹{statement['net_change']}")
    
    # Bank statistics
    print("\n9️⃣ Bank Statistics...")
    stats = BankAccount.get_bank_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n🔟 Testing Security Features...")
    # Test wrong PIN
    print("Testing wrong PIN:")
    savings_acc.withdraw(100, "0000")  # Wrong PIN
    
    # Test account freezing
    print("\nTesting account freeze:")
    checking_acc.freeze_account()
    checking_acc.deposit(100, "5678")  # Should fail
    checking_acc.unfreeze_account("ADMIN123")
    checking_acc.deposit(100, "5678")  # Should work now

except ValueError as e:
    print(f"❌ Error: {e}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n" + "=" * 60)
print("🎉 COMPLETE BANK ACCOUNT PROJECT DEMONSTRATION FINISHED!")
print("=" * 60)