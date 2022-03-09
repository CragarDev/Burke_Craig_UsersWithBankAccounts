from bankAccounts import BankAccount


# * Craig Burke - Assignment: Users With Bank Accounts
#  User class
class User:
    all_users = []

    def __init__(self, data):

        self.name = data["name"]
        self.email = data["email"]
        self.age = data["age"]
        self.user_name = data["user_name"]
        self.has_checking = False
        self.has_savings = False
        User.all_users.append(self)

# t-  ---------------------------------------------------------------------------------

    def openCheckingAccount(self, account_name, interest_rate, amount):
        self.checking = BankAccount(
            self.user_name, "Checking", account_name, interest_rate, amount)
        self.has_checking = True
        return self

    def openSavingsAccount(self, account_name, interest_rate, amount):
        self.savings = BankAccount(
            self.user_name, "Savings", account_name, interest_rate, amount)
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


hattieHam_data = {
    "name": "Harriet Hammer",
    "email": "harham@someemail.com",
    "age": 26,
    "user_name": "hattiHam"
}

pauleyBoy_data = {
    "name": "Paul McCartney",
    "email": "pMc@theBeatles.com",
    "age": 79,
    "user_name": "pauleyBoy"
}

capAmer_data = {
    "name": "Steve Rogers",
    "email": "ImTheBest@avengers.com",
    "age": 180,
    "user_name": "capAmer"
}


# Initialize Users
hattieHam = User(hattieHam_data)
pauleyBoy = User(pauleyBoy_data)
capAmer = User(capAmer_data)
print("")


# info:
hattieHam.display_user_info()
print("")
pauleyBoy.display_user_info()
print("")
capAmer.display_user_info()
print("")

# set up banking accounts
hattieHam.openCheckingAccount(
    "Ham Checking", 3, 600).openSavingsAccount("HH-Retirement", 12, 2500)
pauleyBoy.openSavingsAccount(
    "Pauls Savings", 5, 12000).openCheckingAccount("P-Check", 3, 4500)
capAmer.openSavingsAccount(
    "CaptainAmerica Savings", 7, 15000).openCheckingAccount("CaptainAmerica Checking", 2, 1500)
print("")

#  Make desposits, get interest, make withdrawals
hattieHam.savings.deposit(25).yield_interest().withdraw(300)
pauleyBoy.checking.withdraw(92).deposit(25).yield_interest().withdraw(300)
capAmer.savings.withdraw(605).deposit(25).yield_interest().withdraw(300)
hattieHam.checking.yield_interest().withdraw(600).withdraw(4500)
pauleyBoy.savings.deposit(900).yield_interest().withdraw(500)
print("")

# Make transfers
hattieHam.checking.transfer_money(pauleyBoy, 100)
capAmer.savings.transfer_money(hattieHam, 1000)
pauleyBoy.checking.transfer_money(capAmer, 500)
print("")

#  Display info again
hattieHam.display_user_info()
print("")
pauleyBoy.display_user_info()
print("")
capAmer.display_user_info()
print("")

#  Display Only Bank Info
BankAccount.print_all_balances()
BankAccount.bank_information()
