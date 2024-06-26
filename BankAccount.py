

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """Initialize the bank account with the provided details."""
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """Deposit the given amount to the account and return the amount deposited."""
        self.balance += amount
        return f"Ksh.{amount} deposited successfully."

    def withdraw(self, amount):
        """Withdraw the given amount from the account if sufficient balance is available."""
        if self.balance < amount:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Ksh.{amount} withdrawn successfully."

    def check_balance(self):
        """Print the current balance of the account."""
        print(f"Current balance: Ksh.{self.balance}")

    def customer_details(self):
        """Print the customer details of the account."""
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        print(f"Balance: Ksh.{self.balance}")

account = BankAccount("1234567890", "Wayne Marwa", "2023-01-01", 5000)
print(account.deposit(2000))             
print(account.withdraw(1000))            
print(account.withdraw(7000))            
account.check_balance()                 
account.customer_details()              
