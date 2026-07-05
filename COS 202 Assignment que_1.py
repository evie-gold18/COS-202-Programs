# MATHEMATICAL CALCULATOR

while True:
    print("\n===== MATHEMATICAL CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (\\)")
    print("6. Power (^)")
    print("7. Modulus (%)")
    print("8. Clear")
    print("9. OFF")

    choice = input("Select an operation (1-9): ")

    if choice == "9":
        print("Calculator OFF")
        break

    elif choice == "8":
        print("Screen Cleared")
        continue

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", num1 + num2)

        elif choice == "2":
            print("Answer =", num1 - num2)

        elif choice == "3":
            print("Answer =", num1 * num2)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Answer =", num1 / num2)

        elif choice == "5":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Answer =", num1 // num2)

        elif choice == "6":
            print("Answer =", num1 ** num2)

        elif choice == "7":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Answer =", num1 % num2)

    else:
        print("Invalid choice!")