#Lautaro Possi
#Team Assignment 2
#November 1, 2024


import random  # Import the random module

def guessing_game():
    target = random.randint(1, 10)  # Generate random number between 1 and 10
    print("Please guess number between 1 and 10:")

    while True:
        guess = int(input())  # Get user input as an integer

        # Nested if...else for guessing logic
        if guess < target:
            print("Please guess higher")
        elif guess > target:
            print("Please guess lower")
        else:
            print("Well done, you guessed it")
            break  # End loop if guessed correctly

guessing_game()  # Start the game
