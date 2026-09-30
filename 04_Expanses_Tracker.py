from textwrap import dedent

expenses = []


def add_expense(expenses):
        product = input("Product: ").strip()
        if not product:
                print("You cannot leave this empty!")
                return

        try:
                price = float(input("Price: "))
        except ValueError:
                print("Invalid Price")
                return

        if price < 1:
                print("The price cannot be lower than 1")
                return

        category = input("Category: ").strip()
        if not category:
                print("You acnnot leae this empty!")
                return
        expenses.append({"product":product, "price":price, "category":category})

def list_expenses(expenses):
        if not expenses:
                        print(dedent("""
                        ########################

                        You Have No Expenses Yet.
                        
                        ########################
                        """))
                        return
        print("Your Expansese Are: \n")
        for number, expanse in enumerate(expenses, start=1):
                        product_value = expanse["product"]
                        price_value = expanse["price"]
                        category_value = expanse["category"]
                        print(f"{number}. {product_value} - {price_value} EGP - {category_value}")

def calc_total_value(expenses):
        total = 0
        for expanse in expenses:
                price_value = expanse["price"]
                total += (price_value)
        print(dedent(f"""Your Total Expenses is : {total} EGP"""))

def del_expense(expenses):
        if not expenses:
                print("There's No Expenses to Delete!")
                return
        try:
                user_selected = int(input("What is the number of the Item that you want to delete: "))
        except ValueError:
                print("Please Enter a Valid Item Number")
                return
        if user_selected < 1 or user_selected > len(expenses):
                print("Please Enter a Valid Item Number.")
                return

        item = user_selected - 1
        expenses.pop(item)



while True:
        print(dedent("""
        1. Add Expense
        2. Show Expenses
        3. Show Total
        4. Delete Expanse
        5. Exit
        \n
        """))
        command = input("> ")

        if command == "1":
                add_expense(expenses)

        elif command == "2":
                list_expenses(expenses)

        elif command == "3":
                calc_total_value(expenses)
        
        elif command == "4":
                del_expense(expenses)

        elif command == "5":
                break

        else:
                print("Please Enter a Valid Command")