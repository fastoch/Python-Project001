MAX_LINES = 3       # best practice = use capital letters to declare constant values
MAX_BET = 100
MIN_BET = 1

# First user inputs = deposit + bet
def deposit():
    while True:     # keep asking the user to enter a deposit amount until he gives a valid amount 
        amount = input("How much would you like to deposit? $")
        # I must ensure the user input is valid
        if amount.isdigit():    # check if inpût is a whole number
            amount = int(amount)    # user input is always a string, so I have to convert it
            if amount > 0:
                break           # break the while loop and bring us down to "return amount"
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a positive number!")
    return amount

def get_number_of_lines():
    while True:    
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():    
            lines = int(lines)    
            if 1 <= lines <= MAX_LINES:
                break      
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter the amount of your bet (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a number between ${MIN_BET} and ${MAX_BET}.")
        else: 
            print("Please enter a positive number.")
    return amount
            

# I put my program in the function main() so that if I end my program, I can call this function again to rerun it
def main():                        
    balance = deposit()
    lines = get_number_of_lines()

    # making sure the balance is sufficient to place the bet
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if balance >= total_bet:
            break
        else: 
            print("Your current balance is insufficient to place this bet.")
            print(f"Your current balance: ${balance}. Your bet: ${total_bet}.")

    if lines == 1:
        print(f"Current balance: ${balance}. You are betting ${bet} on {lines} line. Total bet is equal to: ${total_bet}")
    else:
        print(f"Current balance: ${balance}. You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()