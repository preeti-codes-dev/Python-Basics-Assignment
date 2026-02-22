# Q11: Number Pattern Printer


# Logic:
# 1. First display the pattern options to the user.
# 2. Take pattern choice and height as input.
# 3. Use if-elif to decide which pattern to print.

# Pattern 1:
# - For each row i, print numbers from 1 to i.
# - Use nested loop to print increasing numbers.

# Pattern 2:
# - For each row i, print the same number i repeatedly.
# - Use inner loop to repeat the number i times.

# Pattern 3:
# - Start from height and decrease to 1.
# - Print numbers in reverse order for each row.
#
# Pattern 4:
# - First print increasing numbers from 1 to i.
# - Then print decreasing numbers from i-1 to 1.
# - This creates a pyramid-like pattern.

# 4. If user enters invalid choice, display error message.


print("Choose Pattern:")
print("1. Increasing numbers")
print("2. Same number pattern")
print("3. Reverse decreasing")
print("4. Pyramid pattern")

choice = int(input("Enter pattern number (1-4): "))
height = int(input("Enter height: "))

# Pattern 1
if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2
elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3
elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
elif choice == 4:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid choice")