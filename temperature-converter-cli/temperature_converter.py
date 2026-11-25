print("Temperature Converter")

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Quit")

    choice = input("Choose an option (1, 2 or 3): ")

    if choice == "1":
        temperature = float(input("Enter temperature: "))
        result = (temperature * 9/5) + 32
        print(f"Temperature in Fahrenheit: {result:.2f}°F")

    elif choice == "2":
        temperature = float(input("Enter temperature: "))
        result = (temperature - 32) * 5/9
        print(f"Temperature in Celsius: {result:.2f}°C")

    elif choice == "3":
        print("Thanks for using the Temperature Converter!")
        break

    else:
        print("Invalid choice! Please choose 1, 2 or 3.")