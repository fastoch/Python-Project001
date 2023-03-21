# First user inputs = deposit + bet
def deposit():
    while True:     # keep asking the user to enter a deposit amount until he gives a valid amount 
        amount = input("How much would you like to deposit? $")
        # I must ensure the user input is valid
        