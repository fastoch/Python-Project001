MAX_LINES = 3       # best practice = use capital letters to declare constant values

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

# I put my program in the function main() so that if I end my program, I can just call this function again to rerun it
def main():                        
    balance = deposit()
    lines = get_number_of_lines()
    print(balance)

main()