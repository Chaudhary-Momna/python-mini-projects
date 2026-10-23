import os
import random
import string

# ==========================================
# MASTER PASSWORD SETUP / LOGIN LOGIC
# ==========================================
MASTER_FILE = "master.txt"

# Check if Master Password is set for the first time
if not os.path.exists(MASTER_FILE):
    print("==============================")
    print("      FIRST TIME SETUP        ")
    print("==============================")
    new_master = input("Create a new Master Password for your Vault: ")
    with open(MASTER_FILE, "w") as file:
        file.write(new_master)
    print("Master Password created successfully!\n")

# Load the saved Master Password
with open(MASTER_FILE, "r") as file:
    MASTER_PASSWORD = file.read().strip()

# Authentication Process
attempts = 3
authenticated = False

print("==============================")
print("    SECURITY CHECK - VAULT    ")
print("==============================")

while attempts > 0:
    user_input = input("Enter Master Password: ")
    
    if user_input == MASTER_PASSWORD:
        print("\nAccess Granted! Welcome to your Vault.")
        authenticated = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Access Denied! Incorrect password. Attempts left: {attempts}\n")
        else:
            print("\nAccess Denied! Too many wrong attempts. Vault locked!")

# ==========================================
# MAIN VAULT SYSTEM
# ==========================================
if authenticated:
    while True:
        print("\n==============================")
        print("  SMART PASSWORD VAULT MENU  ")
        print("==============================")
        print("1. Generate and Save New Password")
        print("2. View Saved Passwords in Vault")
        print("3. Exit Program")
        
        choice = input("\nWhat would you like to do? (1/2/3): ")

        if choice == "1":
            chars = string.ascii_letters + string.digits + string.punctuation
            length = int(input("How many characters should the password be? "))

            password = ""
            for i in range(length):
                password += random.choice(chars)

            print(f"\nGenerated Password: {password}")

            service_name = input("Which app/website is this password for? ")
            with open("vault.txt", "a") as file:
                file.write(f"{service_name} : {password}\n")

            print("Password successfully saved to Vault!")

        elif choice == "2":
            print("\n--- Your Saved Passwords ---")
            try:
                with open("vault.txt", "r") as file:
                    content = file.read()
                    if content:
                        print(content)
                    else:
                        print("Vault is currently empty!")
            except FileNotFoundError:
                print("No passwords saved yet (Vault file does not exist).")

        elif choice == "3":
            print("\nVault closing... Good bye!")
            break

        else:
            print("\nInvalid option! Please select 1, 2, or 3.")
