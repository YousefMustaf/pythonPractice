import random
import string



def generate_password(min_lenght, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_chars:
            meet_criteria = meet_criteria and has_special

    return pwd


min_lenth = int(input("What is the Minimum Lenght of the password:\n"))
include_nums = input("Do you want your password to include Numbers: Y/N\n").upper() == 'Y'
special_chars = input("Do you want your password to include Special Characters: Y/N\n").upper() == 'Y'
pwd = generate_password(min_lenth, include_nums, special_chars)
print(f"The generated Password is {pwd}")