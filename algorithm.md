# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. Output a welcome message explaining the purpose of the program.

2. Initialize variables:
    - `INITIAL_BALANCE = 1000`
    - `current_balance = INITIAL_BALANCE`
    - `SENTINEL = 'E'` (to exit the loop)
    - `choice = ''` (to store user’s menu choice)


- Function name: choice_deposit
- Parameter: none
- Return: current_balance
3. Set variable `current_balance` to be global 
4. If the choice is 'D' (Deposit):
     1. Prompt the user to enter the amount to deposit.
     2. If the deposit amount is a digit:
          1. Convert the input to an integer.
          2. If deposit amount is less than 0
             1. Output that user input was invalid
          3. Otherwise
             1. Add deposit amount to current balance
             2. Output that deposit was successful and current account balance rounded to the hundredth place
     3. Otherwise:
           1. Output an error message requesting a valid positive number.

- Function name: choice_view_balance
- Parameter: none
- Return: current_balance 
5. Set variable `current_balance` to be global
6. If the choice is 'V' (View Balance)
   1. Output current account balance rounded to the hundredth place

- Function name: withdraw_function
- Parameter: none
- Return: current_balance
7. Set variable `current_balance` to be global
8. if the choice is 'W' (Withdraw):
    1. Prompt the user to enter the amount to withdraw and strip input of white space
    2. If the withdrawal amount is a digit
         1. Convert the input to an integer.
         1. If withdrawal amount is less than 0
            1. Output that input was invalid
         2. Otherwise 
            1. Subtract withdrawal amount from current balance
            2. Output current account balance rounded to the hundredth place
            3. If the variable `current_balance` is less than 0:
                 1.  Output a warning message indicating that the user will be charged 5% interest.
    3. Otherwise
       1. Output an error message requesting a valid positive number.

- Function name: exit_function
- Parameter: none
- Return: end function
9. Set variable `choice` to be global
10. If the choice is 'E' 
   3. Output a message thanking the user and indicate the program is ending.

- Function name: atm_main
- Parameter: none
- Return: 
11. Set variable `choice` to be global
12. Start a while loop that continues until the SENTINEL is entered
    1. Output the menu options:
        - `D - Deposit`
        - `W - Withdraw`
        - `V - View Balance`
        - `E - Exit`
       2. Prompt the user to input their choice, convert it to uppercase, and strip input of white space
       3. If user doesn't input valid input
            1. Output that they must input a valid option