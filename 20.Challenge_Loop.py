"""Challenge: Create and guess the number game! The game requires importing the `random` module and generating a random integer, which has not been covered yet, so the code has been provided. Here, challenge is created the game's logic using variables, loops, and conditional statements.
"""

## Import the random module to generate random numbers
import random

## Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

## Create a variable to hold the number of times a player guessed a number
attempts = 0

## Create a variable to set the maximum number of guesses before the game ends
max_attempts = 5

## Output a message that welcomes the player and tells them how to play
print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it within", max_attempts, "attempts?")

"""Create the game logic in a loop that executes while the player has remaining 
attempts. The player should be able to input a guess and receive output whether 
the guess is correct, too low, or too high. Should the player reach the maximum 
number of attempts without guessing correctly, a message should be displayed 
indicating the game is over and what the number is, and the game (program) ends.
HINT: `input()` always returns a string, but you will be comparing numeric 
values."""

## Execute the code in the loop while `attempts` is less than `max_attempts`
while attempts < max_attempts:  # Output the player's remaining number of attempts
    print("\nAttempts remaining:", max_attempts - attempts)

    # Get the player's guess
    guess = int(input("Enter your guess: "))

    # Determine if the guess is correct, too high, or too low.
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number", secret_number, "correctly!")
        break

    # Increment attempts by 1
    attempts += 1

    # If the player has reached the maximum number of attempts, end the game
    if attempts == max_attempts:
        print(
            "Game over! You ran out of attempts. The secret number was", secret_number
        )
