
# create a list of words
words = ["pyhton", "developer", "console", "variable", "list"]

# keep track of the user's incorrect guesses
incorrect_guesses_left = 6

# main game loop,  while loop will stop when the condition is false
while incorrect_guesses_left > 0:
    print(f"You have {incorrect_guesses_left} guesses left")
    incorrect_guesses_left -= 1
