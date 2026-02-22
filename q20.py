# Q20: Number System Converter

# Logic:
# 1. Create separate functions for conversions.
# 2. Use simple built-in functions.
# 3. Create menu using while loop.
# 4. Repeat until user chooses Exit.


# Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]


# Decimal to Octal
def decimal_to_octal(n):
    return oct(n)[2:]


# Decimal to Hexadecimal
def decimal_to_hexadecimal(n):
    return hex(n)[2:]


# Binary to Decimal
def binary_to_decimal(b):
    return int(b, 2)


# Main Program
while True:
    print("\n=== NUMBER SYSTEM CONVERTER ===")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter decimal number: "))
        print("Binary:", decimal_to_binary(n))

    elif choice == 2:
        n = int(input("Enter decimal number: "))
        print("Octal:", decimal_to_octal(n))

    elif choice == 3:
        n = int(input("Enter decimal number: "))
        print("Hexadecimal:", decimal_to_hexadecimal(n))

    elif choice == 4:
        b = input("Enter binary number: ")
        print("Decimal:", binary_to_decimal(b))

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")