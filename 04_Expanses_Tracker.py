from textwrap import dedent

expenses = []

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
                product = input("Product: ")
                product = product.strip()
                if not product:
                        print("You cannot leave this empty!")
                        continue
                try:
                        price = float(input("Price: "))   

                except ValueError:
                        #       dedent() removes the common indentation while keeping your code nicely formatted.
                        print(dedent("""        
                        #########################################################
                        
                        Oops! Invalid Input Please Enter a Valid Price in Numbers
                        
                        #########################################################
                         """))
                        continue
                if price < 1:
                        print("The Price Cannot be lower than 1, Please Enter a valid Price")
                        continue
                category = input("Category: ")
                category = category.strip()
                if not category:
                        print("You cannot leave this empty!")
                        continue
                expenses.append({"product":product, "price":price, "category":category})
        elif command == "2":
                if not expenses:
                                print(dedent("""
                                ########################

                                You Have No Expenses Yet.
                                
                                ########################
                                """))
                                continue
                print("Your Expansese Are: \n")
                for number, expanse in enumerate(expenses, start=1):
                                product_value = expanse["product"]
                                price_value = expanse["price"]
                                category_value = expanse["category"]
                                print(f"{number}. {product_value} - {price_value} EGP - {category_value}")
        elif command == "3":
                total = 0
                for expanse in expenses:
                        price_value = expanse["price"]
                        total += (price_value)
                print(dedent(f"""Your Total Expenses is : {total} EGP"""))
        
        elif command == "4":
                if not expenses:
                        print("There's No Expenses to Delete!")
                        continue
                try:
                        user_selected = int(input("What is the number of the Item that you want to delete: "))
                except ValueError:
                        print("Please Enter a Valid Item Number")
                        continue
                if user_selected < 1 or user_selected > len(expenses):
                        print("Please Enter a Valid Item Number.")
                        continue

                item = user_selected - 1
                expenses.pop(item)
        elif command == "5":
                break

        else:
                print("Please Enter a Valid Command")