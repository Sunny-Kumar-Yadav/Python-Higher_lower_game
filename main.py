# Importing 
from Higher_lower_art import logo, vs
from game_data import data
import random
from replit import clear

# Function to get random data from game_data
# account_name = account_a["name"]
# account_description = account_a["description"]
# account_country = account_a["country"]
# print(f"Compare A: {account_name}, a {account_description}, from {account_country}")


# Creating a function instead of applying above code seperately to get it in printable format.
def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f" {account_name}, {account_descr},from {account_country}"

# Creating a function to check the guessed answer is correct or not.
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)

# creating a score variable to keep track of score
score = 0

# creating a variable to exit the while loop
game_should_continue = True

# Making account at position B become the next account at position A.
account_b = random.choice(data) # setting it as global scope to use it as a value of account_a in while loop.

# Make the game repeatable
while game_should_continue:
    # Generate random account from the game data.
    account_a = account_b #making account a previous value of account b
    account_b = random.choice(data) # giving account_b a new random value
    
    # regenrate account_b if account_a is same as account_b
    if account_a == account_b: 
      account_b = random.choice(data)
    
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")
          
    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()  
    
    
    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # clear the screen between rounds.
    clear()
    # printing logo again to see it just after the clearing the screen
    print(logo)
    
    # Give user feedback on their guess.
    if is_correct:
        score += 1 # Score keeping.
        print(f"You're right! Current score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")






