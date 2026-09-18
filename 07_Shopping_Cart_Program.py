# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food to Buy (q to Quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the Price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print("----- YOUR CART -----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total is: ${total}")