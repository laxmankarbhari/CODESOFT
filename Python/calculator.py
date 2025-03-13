print("     SIMPLE CALCULATOR       ")

while True:
    num1 = int(input("\nEnter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exit")
    choice = int(input("Choose operation (1-6): "))

    if choice == 1:
        print("Addition is :", num1 + num2)
    elif choice == 2:
        print("Subtraction is :", num1 - num2)
    elif choice == 3:
        print("Multiplication is :", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Math Error: Division operation with zero is undefined !")
        else:
            print("Division is :", num1 / num2)
    elif choice == 5:
        if num2 == 0:
            print("Math Error: Modulus operation with zero is undefined !")
        else:
            print("Modulus is :", num1 % num2)
    elif choice == 6:
        print("\nExiting Calculator. Thank you!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 6.\n")
