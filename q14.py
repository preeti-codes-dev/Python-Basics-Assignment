# Q14: Factorial Calculator


# Logic:
# 1. Take a number from the user.
# 2. Check if the number is negative.
#    - If it is negative, factorial is not defined.
# 3. If the number is 0:
#    - Print 0! = 1 because factorial of 0 is 1.
# 4. If the number is positive:
#    - Start factorial value as 1.
#    - Use a loop from 1 to the given number.
#    - Multiply each number with factorial.
# 5. After the loop ends, print the final factorial result.


# Taking input
num = int(input("Enter a number: "))

# Check if number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")

# If number is 0
elif num == 0:
    print("0! = 1")

# If number is positive
else:
    factorial = 1

    for i in range(1, num + 1):
        factorial = factorial * i

    print(str(num) + "! =", factorial)