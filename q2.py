# Q2: Simple Calculator

# Logic:
# 1. Take two numbers from user.
# 2. Perform addition, subtraction, multiplication, division, modulus and exponent.
# 3. Display all results clearly.


# Taking input from user
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Results:")

    # Addition
    print(num1, "+", num2, "=", num1 + num2)

    # Subtraction
    print(num1, "-", num2, "=", num1 - num2)

    # Multiplication
    print(num1, "*", num2, "=", num1 * num2)

    # Division
    if num2 != 0:
        print(num1, "/", num2, "=", round(num1 / num2, 2))
    else:
        print("Division by zero is not allowed")

    # Modulus
    if num2 != 0:
        print(num1, "%", num2, "=", num1 % num2)
    else:
        print("Modulus by zero is not allowed")

    # Exponentiation
    print(num1, "^", num2, "=", num1 ** num2)

except ValueError:
    print("Invalid input! Please enter numbers only.")