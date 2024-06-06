import random

# create a list of words
words = ["python", "developer", "console", "variable", "list"]

# select a random word from the list 
random_word = random.choice(words)

# display the '_' based on the lenght of the word
guessed_spaces = ["_"] * len(random_word)

# keep track of the user's incorrect guesses
incorrect_guesses_left = 6

# intro
print("Let\'s play a word game!")

# main game loop,  while loop will stop when the condition is false
while incorrect_guesses_left > 0:
    print(f"You have {incorrect_guesses_left} guesses left")

    next_guess = input("Please enter your guess: ")
    if next_guess in random_word:
        for index, letter in enumerate(random_word):
            if letter == next_guess:
                guessed_spaces[index] = next_guess
        print("".join(guessed_spaces))  # print the word and join them with an empty space instead of a list
    else:
        print("Sorry try again!")
        incorrect_guesses_left -= 1
