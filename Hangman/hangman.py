import random

# list of words to choose from
words = ["apple", "banana", "cherry", "orange", "kiwi", "lemon", "melon", "peach"]

# choose a random word from the list
word = random.choice(words)

# create a list of underscores to represent each letter in the word
word_display = ["_" for letter in word]

# create a set to store guessed letters
guessed_letters = set()

# number of guesses allowed
max_guesses = 6

# loop until the game is over
while True:
    # display the word with underscores for missing letters
    print(" ".join(word_display))
    
    # prompt the user for a guess
    guess = input("Guess a letter: ").lower()
    
    # if the guess has already been made, inform the user
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    # add the guess to the set of guessed letters
    guessed_letters.add(guess)
    
    # check if the guess is in the word
    if guess in word:
        print("Correct!")
        # replace underscores with the correct letter
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = letter
    else:
        print("Incorrect!")
        # reduce the number of guesses left
        max_guesses -= 1
    
    # check if the game is over
    if max_guesses == 0:
        print("You lose! The word was:", word)
        break
    elif "_" not in word_display:
        print("You win!")
        break
