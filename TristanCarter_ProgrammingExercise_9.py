#Tristan Carter 11/01/25
#This program will display account holder name, account number, balance, and interest rates.
#It will allow you to deposit and withdraw money, and also adjust and calculate the interest rate.
#It will then show a final balance at the end.

#BankAcct class
class BankAcct:
    def __init__(self, name, account_number, balance=0.0, interest_rate=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = float(balance)
        self.interest_rate = float(interest_rate)

    #Adjusts the interest rate
    def adjust_interest(self, new_rate):
        self.interest_rate = float(new_rate)
        print(f"Interest rate adjusted to {self.interest_rate:.2%}.")

    #Deposit money
    def deposit(self, amount):
        self.balance += float(amount)
        print(f"Deposited ${amount:.2f}.")

    #Withdraw Money
    def withdraw(self, amount):
        self.balance -= float(amount)
        print(f"Withdrew ${amount:.2f}.")

    #Get balance
    def get_balance(self):
        return self.balance

    #Calculate interest
    def calculate_interest(self, days):
        interest_earned = self.balance * (self.interest_rate / 100) * (days / 365)
        return interest_earned

    #Add interest to balance
    def add_interest(self, days):
        interest = self.calculate_interest(days)
        self.balance += interest
        print(f"Interest of ${interest:.2f} for {days} days.")

    #Display name, account number, balance, and interest amounts
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Current Balance: ${self.balance:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}\n")

def test_bank_acct():

    #Create a new account
    new_account = BankAcct("Tristan Carter", "65489951", 1500.0, 1.0)
    print("Initial balance.")
    print(new_account)

    #Depositmoney
    new_account.deposit(1500)
    print(new_account)

    #Withdraw money
    new_account.withdraw(200)
    print(new_account)

    #Calculate and apply interest
    interest = new_account.calculate_interest(60)
    new_account.add_interest(60)
    print(new_account)

    #Adjust interest rate
    new_account.adjust_interest(2.0)
    print(new_account)

    #Calculate and apply interest
    interest = new_account.calculate_interest(60)
    new_account.add_interest(60)
    print(new_account)

    #Get balance
    new_balance = new_account.get_balance()
    print(f"Final balance: ${new_balance:.2f}")

#Run the test function
test_bank_acct()