# Q12: Multiplication Table Generator


# Logic:
# 1. Ask the user to enter a number.
# 2. Ask the user to enter the ending range.
# 3. Use a for loop from 1 to the given range.
# 4. Multiply the number with each value of the loop.
# 5. Print the multiplication result in table format.

# For the full multiplication table (1 to 10):
# 6. Use nested loops.
# 7. Outer loop represents rows (numbers 1 to 10).
# 8. Inner loop represents columns (numbers 1 to 10).
# 9. Multiply row number with column number.
# 10. Print results in grid format using tab space.


# Taking input for single table
num = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print("\nMultiplication Table of", num)

# Printing single table
for i in range(1, end + 1):
    result = num * i
    print(num, "x", i, "=", result)


# Full multiplication table 1 to 10
print("\nFull Multiplication Table (1 to 10)")

for i in range(1, 11):          # Rows
    for j in range(1, 11):      # Columns
        print(i * j, end="\t")
    print()