import time
#We are cerating dictionary called accounts where all costumer info will be stored
accounts = {}



# We are creating "create_account" function


def create_account():
    # Create account_number
    account_number = input("Create account number: ")
    while not account_number.isdigit():
        print("Invalid answer, only numbers are allowed!")
        account_number = input("Create account number again: ")

    # create account_name
    account_name = input("Enter your username: ")
    while account_name.isdigit():
        print("Invalid answer, no numbers allowed!")
        account_name = input("Enter your username again: ")

    # Create password
    account_password = input("Create your password: ")

    # Create a balance
    balance = input("How much do you want to be your balance?: ")
    while not balance.isdigit():
        print("Invalid answer, only numbers are allowed!")
        balance = input("How much do you want to be your balance?: ")

    balance = int(balance)
    
    #This is dictionary for user information
    accounts[account_number] = {
        "account_name": account_name,
        "account_password": account_password,
        "balance": balance
    }

    print(f"Hello {account_name}, your account number is {account_number}, your password is {account_password} and your balance is ${balance}")
    print("\nMake sure you remember all these account details!\n")




# Here we are creating "deposit" functiuon

def deposit():
    #login with account_number
    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name
    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")


    #Login with account_password
    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")

    # Doing a deposit for costumer
    deposit_amount = input("Enter the amount you want to deposit: ")
    while not deposit_amount.isdigit():
        print("Please enter solid numbers!")
        deposit_amount = input("Enter the amount you want to deposit: ")

    deposit_amount = int(deposit_amount)

    # We are adding to old balance new deposit
    accounts[account_number]["balance"] += deposit_amount
    print(f"\nHello {account_name}, your deposit is ${deposit_amount} and your new balance is ${accounts[account_number]['balance']}\n")










# Here we are creating "withdraw" function

def withdraw():

    #login with account_number

    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name

    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")

    #Login with account_password

    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")

    #We are asking costumer withdraw money

    withdraw_amount = input("Enter how much you want to withdarw: ")
    while not withdraw_amount.isdigit():
        print("Invalid answer,Only numbers!!!")
        withdraw_amount = input("Enter how much you want to withdarw: ")
    
    # We are stealing to old balance new withdraw
    withdraw_amount = int(withdraw_amount)
    accounts[account_number]["balance"] -= withdraw_amount

    print(f"\nHello {account_name}, your deposit is ${withdraw_amount} and your new balance is ${accounts[account_number]['balance']}\n")





# Here we ara creating "check_balance" function

def check_balance():
    #login with account_number

    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name
    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")

    #Login with account_password
    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")    

    # Showing costumer his balance
    print(f"\nHello {account_name}, your balance is ${accounts[account_number]['balance']}\n")





# Here we are creating "account_info" function

def account_info():

    # Login with account_number

    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name

    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")

    #Login with account_password

    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")

    # Here we are showing costumer his account_info
    print(f"Your account_name is {accounts[account_number]["account_name"]}, your password is {accounts[account_number]["account_password"]} and your account_number is {account_number}")


#Here we are creating "update_info" function

def update_info():

    #Login with account_number

    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name

    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")
    
    #Login with account_password

    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")

    #Here we are asking costumer new account_number
    account_number = input("Create account number: ")
    while not account_number.isdigit():
        print("Invalid answer, only numbers are allowed!")
        account_number = input("Create account number again: ")

    #Here we are replacing old account_number to new account_number

    accounts[account_number] = account_number


    

    print(f"\nYour new account number is {account_number}\n")



    


# Here we are creating "delete_account" function


def delete_account():
    #Login with acoount_number

    account_number = input("Enter your account number: ")
    while account_number not in accounts:
        print("Account not found, try again!")
        account_number = input("Enter your account number: ")

    print("Account successfully found. Now enter your account info!")

    #Login with account_name

    account_name = input("Account name: ")
    while account_name != accounts[account_number]["account_name"]:
        print("Invalid account name, try again!")
        account_name = input("Account name: ")

    #Login with account_password

    account_password = input("Account password: ")
    while account_password != accounts[account_number]["account_password"]:
        print("Invalid account password, try again!")
        account_password = input("Account password: ")

    print("\nSuccessfully logged in.\n")

    #Here we are deleting old account
    del accounts[account_number]
    print("\nAccount succesfully deleted.\n")





# Here we are creating "main_menu" function

def main_menu():
    while True:
        print("\nWelcome to atuka's Bank")
        print("0. Create account/Change account")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdarw")
        print("4. Account info")
        print("5. Uptade accounts number")
        print("6. Delete account")
        print("7. Exit")


        option = input("\nEnter choice: ")

    # Here we have match/case box like(if/else)
        match option:
            case "0":
                create_account()
            case "1":
                check_balance()
            case "2":
                deposit()
            case "3":
                withdraw()
            case "4":
                account_info()
            case "5":
                update_info()
            case "6":
                delete_account()
            case "7":
                print("\nThanks for using Atuka's Bank")
                break
            case _:
                print("Invalid number!!!")



#With this function we gonna do enter ilusion with time librabry,after that "Connecting to the atuka's Bank..." code will stop  3 second and after that "Succesfully connected to the Atuka's Bank" this wiil be shown and our bank will be appear

def connect():
    print("Click any button for start: ") 
    input()
    print("Connecting to the atuka's Bank...")
    time.sleep(3)
    print("\nSuccesfully connected to the Atuka's Bank\n")





# We are running main_manu function
connect()
main_menu()