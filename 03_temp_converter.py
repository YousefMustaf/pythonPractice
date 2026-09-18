unit = input('IS this temperature in Celsius or Fahrenheit (C / F): ').upper()
temp = int(input("Enter the Temp: "))

temp_in_Fahrenheit = round((temp * 9 / 5) + 32, 1)
temp_in_Celcius = round((temp - 32) * 5 / 9, 1)

if unit == "C":
    print(f'The tempreture in Fahrenheit is {temp_in_Fahrenheit}')
elif unit == "F":
    print(f"The Temperature in Celsius is {temp_in_Celcius}")
else:
    print(f"{unit} is not a valid Tempreture Unit")