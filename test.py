# Functions = A block of reusable CODE
#               place () after the function name to invoke it

# let's take an example:

# print("HappyBirthDay")
# print("You are Old")
# print("Happy Birthday to you")

# print("HappyBirthDay")
# print("You are Old")
# print("Happy Birthday to you")

# print("HappyBirthDay")
# print("You are Old")
# print("Happy Birthday to you")


# def greet(name):
#     print(f"HappyBirthDay {name}")
#     print("You are Old")
#     print("Happy Birthday to you")

# greet(input("Enter Your Name Please: "))

# def display_invoice(username, amount, due_date):
#     print(f'Hello {username}')
#     print(f'Your Bill of ${amount:.2f} is due: {due_date}')


# display_invoice("Joe", 30.11, "01/02")

# return = statment used to end a function
#           and send a result back to the caller


# def add(x, y):
#     z = x + y
#     return z


# def subtract(x, y):
#     z = x - y
#     return z


# def multiply(x, y):
#     z = x * y
#     return z


# def devide(x, y):
#     z = x / y
#     return z


# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(devide(1, 2))


# def create_name(first, last):
#     first = first.upper()
#     last = last.upper()
#     return first + " " + last

# full_name = create_name("yousef", "mostafa")
# print(full_name)

# Parameter: is the input that you define for your function.
# Argument : is the value giving to the parameter at it's same index.

# in programming we have 2 kidns of functions: 


# # 1. Perform a TASK
# def greet(name):
#     print(f"Hello {name}")
# greet(input("Enter Your Name: "))

#     # 2. Return a Value

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting(input("Enter Your Name: "))
# print(message)


# as we mentioned before the parameters are index sensetive to avoide troubles like this we use the comming method by reassigning the value of the parameter by the name of it.
# def increment(number, by):
#     return number / by

# result = increment(by=1, number=2) # Now it will not get bugs because of the index mismatch.
# print(result)

# and this was short explaination for the KEYWORD ARGUMENTS

 
 ############################
 # Default Arguments

# def increment(number, by=1): #buy adding a value to the parameter from the beginning we make it optional to input the value of it as an argument, but if we added a specefic value as an argument the one in the begging will get overrided.
#     return number + by

# result = increment(2, 4) 
# print(result)

# def multiply(*numbers): 
    
    # This * before the parameter creates a tupe with the variable name "numbers" so any argument we type when we are callin the funtion being added to the parameter with no limits sowe can unlimitedly add arguments to our function.
    
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))


# def save_user(**user):
#     print(user)

# save_user(id=1, name="john", age=22)

# FIRST ONE
def fizz_buzz(Number):
        if (Number % 3 == 0) and (Number % 5 == 0):
            return "FizzBuzz"
        elif Number % 3 == 0:
            return "Fizz"
        elif Number % 5 == 0:
            return "Buzz"
        else:
            return Number

result = fizz_buzz(int(input("Enter Your Number: ")))
print(result)

# SECOND ONE 
for i in range(1, 16):
    if (i % 3 == 0) and (i % 5 == 0):
        print(f"{i} FizzBuzz")
    elif i % 3 == 0:
        print(f"{i} Fizz")
    elif i % 5 == 0:
            print(f"{i} Buzz")
    else:
         print(i)