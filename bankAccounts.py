
# * Craig Burke - Assignment: Users With Bank Accounts
#  BankAccount Class

class BankAccount:
    all_bank_accounts = []
    bank_name = "Money Good Financial"
    user_count = 0

    def __init__(self, user_name, acct_type, account_name="my checking", int_rate=5.5, balance=0):
        self.user_name = user_name
        self.account_name = account_name
        self.interest_rate = int_rate * .01
        self.account_balance = balance
        self.account_type = acct_type
        BankAccount.all_bank_accounts.append(self)
        BankAccount.user_count += 1

    def deposit(self, amount):
        self.account_balance += amount
        print(f"-=-=- {self.user_name} -=-=-")
        print(
            f"Your deposit of ${amount:,.2f} into your {self.account_type} Account: '{self.account_name}' has been accepted!")
        self.new_balance()
        print("")
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
            print(f"-=-=- {self.user_name} -=-=-")
            print(
                f"Your withdrawal of ${amount:,.2f} from your {self.account_type} Account: '{self.account_name}' has been completed!")
            self.new_balance()
            print("")
            return self
        else:
            print(
                f"Your {self.account_type} Account: '{self.account_name}' has")
            print("Insufficient funds: Charging a $5.00 fee!")
            self.new_balance()
            print("")
            self.account_balance -= 5
        return self

    def display_account_info(self):
        print(f"-=-=- {self.user_name} -=-=-")
        print(
            f"The balance in your {self.account_type} account is: ${self.account_balance:,.2f}")
        print("")
        return self

    def new_balance(self):
        print(f"Your balance is: ${self.account_balance:,.2f}")
        return self

    def yield_interest(self):
        if self.account_balance > 0:
            intIncrease = self.account_balance * self.interest_rate
            self.account_balance += intIncrease
            print(f"-=-=- {self.user_name} -=-=-")
            print(
                f"You have received ${intIncrease:,.2f} interest on your {self.account_type} Account: '{self.account_name}'!")
            self.new_balance()
            print("")
            return self
        else:
            print(f"-=-=- {self.user_name} -=-=-")
            print("You do not have enough funds to earn interest.")
            print("")
        return self

    def transfer_money(self, other_user, amount=0):
        self.account_balance -= amount
        other_user.checking.account_balance += amount
        print(f"-=-=- {self.user_name} -=-=-")
        print(
            f"{self.account_name}, the transfer to {other_user.name}\nfor the amount of {amount}, has been processed.\nThank You!")
        self.new_balance()
        print("")

    @ classmethod
    def bank_information(cls):
        print(f"======= {cls.bank_name} =======")
        usernames_list = []
        print("--- Users:")
        for each_user in cls.all_bank_accounts:
            if (each_user.user_name in usernames_list):
                continue
            else:
                usernames_list.append(each_user.user_name)
        for i in range(len(usernames_list)):
            print(f"  {usernames_list[i]}")
            for each_account in cls.all_bank_accounts:
                if each_account.user_name == usernames_list[i]:
                    print(f"    - {each_account.account_name}")
                else:
                    continue
        print("")
        print(f"Number of users: {len(usernames_list)}")
        cls.print_all_balances()

    @ classmethod
    def print_all_balances(cls):
        total_sum = 0
        for each_account in cls.all_bank_accounts:
            total_sum += each_account.account_balance
        print(f"The balance of all the accounts is: ${total_sum:,.2f}")
        print("")

    @ staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount < 0):
            return False
        else:
            return True
