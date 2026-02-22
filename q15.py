# Q15: Prime Number Checker


# Logic:
# 1. Take a number from the user.
# 2. If the number is less than or equal to 1,
#    then it is not a prime number.
# 3. If the number is greater than 1:
#    - Assume it is prime (prime = True).
#    - Check divisibility from 2 to number-1.
# 4. If the number is divisible by any value in that range:
#    - Set prime = False.
#    - Stop checking using break.
# 5. After the loop:
#    - If prime is still True, it is a prime number.
#    - Otherwise, it is not a prime number. 


num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")

else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")