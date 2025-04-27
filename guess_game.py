import random

def guess_the_number():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < number_to_guess:
                print("🔼 Too low! Try again.")
            elif guess > number_to_guess:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break  # Exit the loop if guessed correctly
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
