"""A number-guessing game."""

from random import randint

# Game Overview:
# Computer chooses a random number between 1-100 
# Ask the user to guess the number 
# Once the user guesses, the computer tell tells the user if their guess is too low or too high 
# The game is over once the user guesses the random number

# Store number of user guesses
num_guesses = 0

# Random number between 1 and 100
number = randint(1, 100)

# Get user's name and then greet user
user_name = input("Hello there! Please enter your name: ")
print(f"Welcome, {user_name}!")
print("I'm thining of a number between 1 and 100. Can you guess what the number is?")

# Loop to handle user guess input
while True:
    user_guess = input("What's your guess: ")

    # Check if user guess is a valid number
    try:
        user_guess = int(user_guess)
    except ValueError:
        print(f'Sorry, {user_guess} is not a valid number. Please try again.')
        continue

    # Check is user guess is between 1 and 100
    if user_guess < 1 and user_guess > 100:
        print('Please guess a number between 1 and 100: ')
        continue

    # Store number of user attempts(guesses)
    num_guesses += 1



