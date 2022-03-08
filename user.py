from bankAccounts import BankAccount


# * Craig Burke - Assignment: Users With Bank Accounts
#  User class
class User:

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.has_checking = False
        self.has_savings = False

    def openCheckingAccount(self, account_name, interest_rate, amount):
        self.checking = BankAccount(
            "Checking", account_name, interest_rate, amount)
        self.has_checking = True
        return self

    def openSavingsAccount(self, account_name, interest_rate, amount):
        self.savings = BankAccount(
            "Savings", account_name, interest_rate, amount)
        self.has_savings = True
        return self

    def display_user_info(self):
        print(f"======== User: {self.name} ==========")
        print(f"Name: {self.name}\nEmail: {self.email}\nAge: {self.age}")
        if (self.has_checking):
            print(
                f"Checking Account: {self.checking.account_name}\n  - Interest Rate: {self.checking.interest_rate * 100}%\n  - Balance: ${self.checking.account_balance:,.2f}")
        else:
            print("No Checking Account found")
        if (self.has_savings):
            print(
                f"Savings Account: {self.savings.account_name}\n  - Interest Rate: {self.savings.interest_rate * 100}%\n  - Balance: ${self.savings.account_balance:,.2f}")
        else:
            print("No Savings Account found")
        print("====== Thank You! =======")
        print("")
        return self


# Initialize Users
hattieHam = User("Harriet Hammer", "harham@someemail.com", 26)
pauleyBoy = User("Paul McCartney", "pMc@theBeatles.com", 79)
print("")
# info:

hattieHam.display_user_info()
print("")
pauleyBoy.display_user_info()
print("")

# set up accounts
hattieHam.openCheckingAccount("Ham Checking", 6, 300)
hattieHam.openSavingsAccount("Retirement", 12, 25000)
pauleyBoy.openSavingsAccount(
    "Pauls Savings", 9, 6000).openCheckingAccount("P-Check", 3, 4500)

hattieHam.savings.yield_interest().deposit(25).withdraw(300)
pauleyBoy.checking.withdraw(92)
pauleyBoy.savings.withdraw(605)
hattieHam.checking.yield_interest().withdraw(600).withdraw(4500)
hattieHam.display_user_info()
pauleyBoy.savings.deposit(900).yield_interest().withdraw(500)


hattieHam.display_user_info()
print("")
pauleyBoy.display_user_info()
print("")

# *    ---------- working on the transfer ---------------
hattieHam.checking.transfer_money(pauleyBoy, 100)
hattieHam.display_user_info()
print("")
pauleyBoy.display_user_info()
print("")

BankAccount.print_all_balances()
BankAccount.bank_information()
