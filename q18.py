# Q18: Calculator using Functions

# Logic:
# 1. Create separate functions for each operation.
# 2. Create a main calculator() function with menu.
# 3. Take user input.
# 4. Call the correct function.
# 5. Repeat until user chooses Exit.

import math   # For square root


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Modulus
def modulus(a, b):
    return a % b


# Power
def power(a, b):
    return a ** b


# Bonus: Square Root
def square_root(a):
    if a < 0:
        return "Square root not defined for negative numbers"
    return math.sqrt(a)


# Bonus: Percentage
def percentage(a, b):
    return (a / 100) * b


# Main Calculator Function
def calculator():

    while True:
        print("\nCALCULATOR MENU")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 9:
            print("Exiting Calculator...")
            break

        # For square root only one input needed
        if choice == 7:
            a = float(input("Enter number: "))
            print("Result:", square_root(a))

        # For percentage
        elif choice == 8:
            a = float(input("Enter percentage value: "))
            b = float(input("Enter total value: "))
            print("Result:", percentage(a, b))

        # For other operations (need two numbers)
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(a, b))

            elif choice == 2:
                print("Result:", subtract(a, b))

            elif choice == 3:
                print("Result:", multiply(a, b))

            elif choice == 4:
                print("Result:", divide(a, b))

            elif choice == 5:
                print("Result:", modulus(a, b))

            elif choice == 6:
                print("Result:", power(a, b))

            else:
                print("Invalid choice")


# Call the calculator
calculator()