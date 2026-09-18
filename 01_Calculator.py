import math
operator = input("Enter an Operator +\n -\n *\n /\n\n > ")

num1 = float(input("Enter the First Number"))
num2 = float(input("Enter the Second Number"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid Operator!")