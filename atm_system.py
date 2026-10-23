# Class definition for BankAccount representing the ATM logic
class BankAccount:
    # Constructor method to initialize account attributes
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder  # Public attribute: Account holder's name
        self.__balance = balance  # Private attribute: Stores account balance securely
        self.__pin = pin  # Private attribute: Stores secret 4-digit PIN

    # Helper method to verify if the entered PIN matches the account PIN
    def verify_pin(self, entered_pin):
        if entered_pin == self.__pin:
            return True
        else:
            return False

    # Method to check and display current account balance
    def check_balance(self, entered_pin):
        if self.verify_pin(entered_pin):
            print(f"True!\nYour balance is Rs.{self.__balance}")
        else:
            print(f"False!\nIncorrect pin")

    # Method to deposit money into the account
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount  # Update balance with deposited amount
            print(f"The amount {amount} is successfully deposited!")
        else:
            print(f"{amount} is Invalid amount!")

    # Method to withdraw money with validation checks
    def withdraw(self, amount, entered_pin):
        # Guard Check 1: Verify PIN security
        if not self.verify_pin(entered_pin):
            print("Invalid Pin!")
        # Guard Check 2: Check if requested amount exceeds available balance
        elif amount > self.__balance:
            print("Insufficient Balance!")
        # Guard Check 3: Check for zero or negative withdrawal amounts
        elif amount <= 0:
            print("Invalid Amount!")
        # Successful transaction: Deduct amount from balance
        else:
            self.__balance -= amount
            print(f"Rs. {amount} is withdrawn!")
            print(f"Remaining Balance: Rs. {self.__balance}")


# ==========================================
# User Registration and Setup
# ==========================================
print("=== 🏧 Welcome to Python Bank ATM System 🏧 ===")

# Collect initial user input to set up the account
user_name = input("Enter your name: ")
user_balance = float(input("Enter your balance: "))
user_pin = input("Enter 4-Digit pin: ")

# Create a new BankAccount instance (object) using provided inputs
user_acc = BankAccount(user_name, user_balance, user_pin)
print(f"Congratulations! {user_name}, your account is created.")


# ==========================================
# Interactive ATM Menu Loop
# ==========================================
while True:
    # Display available ATM options to the user
    print("\n------------------------------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("------------------------------")

    # Get option choice from user
    choice = input("Choose your option(1-4): ")

    # Option 1: View current balance
    if choice == "1":
        pin = input("Enter your pin: ")
        user_acc.check_balance(pin)

    # Option 2: Add funds to account
    elif choice == "2":
        amt = float(input("How much money you want to deposit? "))
        user_acc.deposite(amt)

    # Option 3: Withdraw funds from account
    elif choice == "3":
        amt = float(input("How much money you want to withdraw? "))
        pin = input("Enter your pin: ")
        user_acc.withdraw(amt, pin)

    # Option 4: Terminate the loop and exit the system
    elif choice == "4":
        print("\nThanks for using the ATM! Allah Hafiz 👋")
        break  # Exit the while loop

    # Handle invalid menu selections
    else:
        print("\n⚠️ Wrong option! Please select an option between 1 and 4.") 
