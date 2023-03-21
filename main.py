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

