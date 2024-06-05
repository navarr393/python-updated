import random

# Types of chars the user can chose from
lowercase = "abcdefghijklmnopqrstuvwxyz"
upppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%&*?"

# Ask the user how long the password should be
password_lenght = int(input("How long would you like the password to be?: "))

# Ask the user for parameters
use_lowercase = input("Do you want to use lowercase characters (Y/N)?")
use_uppercase = input("Do you want to use uppercase characters (Y/N)?")
use_numbers = input("Do you want to use numbers (Y/N)?")
use_symbols = input("Do you want to use symbols (Y/N)?")

password = ""
character_options = ""

# Add the parameters the user chose 

if use_lowercase == "Y":
    character_options += lowercase

if use_uppercase == "Y":
    character_options += upppercase

if use_numbers == "Y":
    character_options += numbers

if use_symbols == "Y":
    character_options += symbols


for i in range(password_lenght):
    random_letter_index = random.randint(0, len(character_options) - 1)
    random_letter = character_options[random_letter_index]
    password = password + random_letter

print(password)