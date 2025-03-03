def length_converter():
    print("\nLength Converter:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km is {miles:.2f} miles")
    elif choice == '2':
        miles = float(input("Enter distance in miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is {km:.2f} km")
    else:
        print("Invalid choice!")

def weight_converter():
    print("\nWeight Converter:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kg is {pounds:.2f} lbs")
    elif choice == '2':
        pounds = float(input("Enter weight in pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} lbs is {kg:.2f} kg")
    else:
        print("Invalid choice!")

def temperature_converter():
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\n")
