import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        # If the guess is too high
        elif guess > secret_number:
            print("Too high! Try again.")
        # If the guess is too low
        else:
            print("Too low! Try again.")

# Run the game
guess_number()
