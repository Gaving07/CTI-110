# Name: Gavin Guy
# Date: 11/01/2026
# Assignment: AI Python Project - Number Guessing Game
# Description: A simple game where the user guesses a randomly selected number.

import random

def play_game():
    # Choose a random number between 1 and 100.
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        guess_text = input("Enter your guess: ")

        # Make sure the user enters a whole number.
        if not guess_text.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_text)

        # Make sure the guess is within the allowed range.
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break


def main():
    print("Welcome to the Number Guessing Game!")

    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if play_again not in ("yes", "y"):
            print("Thanks for playing!")
            break


# Start the game.
if __name__ == "__main__":
    main()
