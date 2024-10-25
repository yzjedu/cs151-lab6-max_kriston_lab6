# Programmers: Krishon Pinkins and Max Rice
# Course:  CS151, Professor Zee
# Due Date: 10/24/24
# Programming Assignment: LAB 06
# Problem Statement: You need to refactor the ATM application so that it has proper error checking and functions.
# Data In: User input choice, deposit amount, withdrawal amount
# Data Out:  Current Balance
# Credits: N/A
# Display the purpose of the program

print("Welcome to the ATM program! This program allows you to interact with your account balance.")


# Initialize variables
INITIAL_BALANCE = 1000
current_balance = INITIAL_BALANCE
SENTINEL = 'E'
choice = ''


# Function for the deposit choice
def choice_deposit():
    global current_balance
    if choice == 'D':
        deposit_amount = input("Enter the amount to deposit: ").strip()

        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
# Checks users input amount, and outputs error if present
            if deposit_amount < 0:
                print("Error: Please enter a positive number.")
            else:
                current_balance += deposit_amount
                print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
        else:
            print("Error: Please enter a valid number.")
            return current_balance
# Function for the view balance choice
def choice_view_balance():
    global current_balance
    if choice == 'V':
        # Clear the screen and show the balance
        print(f"Your current balance is ${current_balance:.2f}.")
    return current_balance
# Function for the withdrawal choice
def choice_withdraw():
    global current_balance
    if choice == 'W':
        withdraw_amount = input("Enter the amount to withdraw: ").strip()

        if withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
# Checks users input amount, and outputs error if present
            if withdraw_amount < 0:
                print("Error: Please enter a positive number.")
            else:
                current_balance -= withdraw_amount
                print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")

                # Warning if the balance is negative
                if current_balance < 0:
                    print("❕ Warning: You have a negative balance. You will be charged 5% interest.")
        else:
            print("Error: Please enter a valid number.")
            return current_balance
# Function for the exit choice
def choice_exit():
    if choice == 'E':
        print("Thank you for using the ATM program. Goodbye!")
        return choice
# Main function to process atm
def atm_main():
    global choice
    while choice.upper() != SENTINEL:
    # Display the menu
        print("\nPlease select an option:"
              "\n\t D - Deposit"
              "\n\t W - Withdraw"
              "\n\t V - View Balance"
              "\n\t E - Exit")
# Asks user to input choice, convert it to uppercase, and strip it of whitespace
        choice = input("Your choice: ").strip().upper()
# Invokes choice functions
        choice_deposit()
        choice_view_balance()
        choice_withdraw()
        choice_exit()
# If user input is not any of the valid choice and output error
        if choice != 'D' or choice != 'W' or choice != 'V' or choice != 'E':
            print("Please enter a valid option.")
    return
# Invoke main atm  function
atm_main()