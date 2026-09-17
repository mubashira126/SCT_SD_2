import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Get the user's guess
        guess = input("Enter your guess: ")

        # Make sure they typed a valid number
        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        attempts += 1

        # Compare guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}. You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    guess_the_number()