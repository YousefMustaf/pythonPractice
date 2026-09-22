operation = input("Enter an Operator \n+ \n- \n* \n/\n> ")
num1 = float(input("Enter the First Number"))
num2 = float(input("Enter the Second Number"))


if operation == '+':
    print(round(num1 + num2))
elif operation == '-':
    print(round(num1 - num2))
elif operation == '*':
    print(round(num1 * num2))
elif operation == '/':
    print(round(num1 / num2))
else:
    print(f"\"{operation}\" is not a valid Operator, Please Enter a Valid Operator")

