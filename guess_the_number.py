import random  # import the random module to generate random numbers

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize the number of guesses to 0
num_guesses = 0

# Prompt the user to enter a guess
print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")

# Loop until the user guesses the correct number
while True:
    guess = input("Enter your guess: ")
    num_guesses += 1  # increment the number of guesses by 1 for each guess

    # Make sure the user entered a valid number
    try:
        guess = int(guess)  # convert the guess to an integer
    except:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue  # if the input is invalid, skip to the next iteration of the loop

    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break  # if the guess is correct, exit the loop using the 'break' keyword
    elif guess < number:
        print("Your guess is too low. Please try again.")
    else:
        print("Your guess is too high. Please try again.")
