weight = int(input("Enter Your Weight: "))
weight_unit = input('Kilograms or Pounds? (K or L): ').upper()
weight_in_pounds = weight / 0.45
weight_in_kilograms = weight * 0.45

if weight_unit == "K":
    result = (f"Your Weight in Pounds is {round(weight_in_pounds,2)} LBS")
elif weight_unit == "L":
    result = (f"Your Weight in Pounds is {round(weight_in_kilograms,2)} KG")
else:
    result = (f"{weight_unit} is not a valild Weight Unit")

print(result)