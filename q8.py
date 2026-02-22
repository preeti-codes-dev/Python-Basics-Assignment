# Q8: Leap Year Checker

# Take year input
year = int(input("Enter a year: "))

# Check leap year step by step
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
            print("Reason: It is divisible by 400.")
        else:
            print(year, "is NOT a Leap Year")
            print("Reason: It is divisible by 100 but not by 400.")
    else:
        print(year, "is a Leap Year")
        print("Reason: It is divisible by 4 but not by 100.")
else:
    print(year, "is NOT a Leap Year")
    print("Reason: It is not divisible by 4.")