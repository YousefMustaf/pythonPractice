import string

letters = string.ascii_letters
upper_letters = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation

passWord = input("Enter Your Password: ")
lenght = False
has_upper = False
has_numbers = False
has_special = False


for char in passWord:
    if len(passWord) >= 8:
        lenght = True

    if char in upper_letters:
        has_upper = True

    if char in numbers:
        has_numbers = True

    if char in special_chars:
        has_special = True

if len(passWord) < 8:
    print("Password Cannot be Below 8 Characters")
    if " " in passWord:
        print("Password Cannot Contain Empty Spaces")
    pass
elif " " in passWord:
    print("Password Cannot Contain Empty Spaces")
    pass
else:
    print(f"Lenght: {lenght}")
    print(f"Has Upper: {has_upper}")
    print(f"Has Numbers: {has_numbers}")
    print(f"Has Special Characters {has_special}")
    print("")
    print("")
    print("")
    print("#############################")
    print ("")
    if lenght and has_numbers and has_special and has_upper:
        print("Password Strenght : Strong")
    elif lenght and (has_special and has_upper) or lenght and (has_numbers and has_special) or lenght and (has_numbers and has_upper):
        print("Password Strenght: Medieum")
    else:
        print("Password Strenght: Easy")
    print("")
    print("#############################")