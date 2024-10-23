# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code... 
function name: atm_main
parameter: none
return: whole program

Function name: deposit_func
parameter: none
return:new balance

Function name: view_function
parameter: none
return: new balance

function: withdraw_function
parameter: none
return: balance

function: exit_function
parameter: none
return: end function





 
1. Output a welcome message explaining the purpose of the program.

2. Initialize variables:
    - `INITIAL_BALANCE = 1000`
    - `current_balance = INITIAL_BALANCE`
    - `SENTINEL = 'E'` (to exit the loop)
    - `choice = ''` (to store user’s menu choice)


- Function name: deposit_func
- parameter: none
- return:new balance
  3. If the choice is 'D' (Deposit):
       1. Prompt the user to enter the amount to deposit.
       2. Check if the deposit amount is a valid positive integer:
            1. Convert the input to an integer.
            1. If the amount is positive, add it to `current_balance`.
            1. Display the new balance to the user.
       3. otherwise:
             1. Output an error message requesting a valid positive number.

- Function name: view_function
- parameter: none
- return: new balance 
  4. if the choice is 'V' (View Balance):
      1. Output the current balance to the user.

- function: withdraw_function
- parameter: none
- return: balance
   5. if the choice is 'W' (Withdraw):
       1. Prompt the user to enter the amount to withdraw.
       2. Check if the withdrawal amount is a valid positive integer:
            1. Convert the input to an integer.
            1. If the amount is positive, subtract it from `current_balance`.
            1. Display the new balance to the user.
            1. If the `current_balance` becomes negative:
                 1.  Output a warning message indicating that the user will be charged 5% interest.
          3. otherwise:
             1. Output an error message requesting a valid positive number.

- function: exit_function
- parameter: none
- return: end function             
   6. if the choice is 'E' (Exit):
       - Output a message thanking the user and indicate the program is ending.

   7. Otherwise, if the choice is not one of the valid options:
       - Output an error message requesting a valid option (D, W, V, or E).

8. Output a message indicating the ATM program has ended.

- function name: atm_main
- parameter: none
- return: program
9. Start a while loop that continues until the user enters 'E' to exit:
   1. Display the menu options:
       - `D - Deposit`
       - `W - Withdraw`
       - `V - View Balance`
       - `E - Exit`
   2. Prompt the user to input their choice and convert it to uppercase.