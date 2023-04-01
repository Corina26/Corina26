# Note: Functions that are associated with classes are called methods.

# We have to create a class to represent bank account. 
# functionalities for this account are:
#Initialize the bank account with an initial balance.
#Deposit a specified amount into the account.
# Withdraw a specified amount from the account, but do not allow overdrawing.
# Check the account balance.

# When we create a instance from Bank Account class, this action actually represents
# opening a new bank account. 
# IN the account we have functionalities,
# like, withdrawal, deposit, check balance


class BankAccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance


    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw because there is not enough funding.")
        elif amount_to_withdraw <= self.balance:
                print( f"You withdrew ${amount_to_withdraw}")
                self.balance -= amount_to_withdraw
                print(f"Your balance of the acccount is {self.balance}")

    def deposit(self,amount_to_be_deposited):
        self.balance += amount_to_be_deposited 
        print(f"You succesfully deposit ${amount_to_be_deposited}")
        print(f"Your updated balance of the account is ${self.balance}")           
    
    def check_balance(self):
        print(f"Your balance of account is ${self.balance}")
        # Let's also return the current balance as a value maybe we could later use as 
        # a variable somewhere
        return self.balance



# Note: Functions that are associated with classes are called methods.

# We have to create a class to represent bank account. 
# functionalities for this account are:
#Initialize the bank account with an initial balance.
#Deposit a specified amount into the account.
# Withdraw a specified amount from the account, but do not allow overdrawing.
# Check the account balance.

# When we create a instance from Bank Account class, this action actually represents
# opening a new bank account. 
# IN the account we have functionalities,
# like, withdrawal, deposit, check balance


class BankAccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance


    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw > self.balance:
            print("You cannot withdraw because there is not enough funding.")
        elif amount_to_withdraw <= self.balance:
                print( f"You withdrew ${amount_to_withdraw}")
                self.balance -= amount_to_withdraw
                print(f"Your balance of the acccount is {self.balance}")

    def deposit(self,amount_to_be_deposited):
        self.balance += amount_to_be_deposited 
        print(f"You succesfully deposit ${amount_to_be_deposited}")
        print(f"Your updated balance of the account is ${self.balance}")           
    
    def check_balance(self):
        print(f"Your balance of account is ${self.balance}")
        # Let's also return the current balance as a value maybe we could later use as 
        # a variable somewhere
        return self.balance


initial_balance=int(input("Welcome to our bank to create an account please enter initial deposit"))

acct = BankAccount(initial_balance)

print("Your account has been succesfully created.")
acct.check_balance()

print("To withdraw press 1, press2 for deposit")
user_choice = input()
if user_choice == "1":
    withdraw_amt = int(input("Enter the amount you want to withdraw"))
    acct.withdraw(withdraw_amt)
elif user_choice == "2":
    deposit_amt = int(input("Enter the amount you want to deposit"))
    acct.deposit(deposit_amt)
else:
    print("Invalid option.")
