def calculator():
    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Floor Division")
        print("6. Modulus")
        print("7. Exponentiation")
        print("8. Exit")
        choice = input("Enter choice (1-8): ")
        cases = {
            '1': num1 + num2,
            '2': num1 - num2,
            '3': num1 * num2,
            '4': num1 / num2,
            '5': num1 // num2,
            '6': num1 % num2,
            '7': num1 ** num2,
        }
        if choice in cases:
            print(f"The result is: {cases[choice]}")
        elif choice == '8':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()