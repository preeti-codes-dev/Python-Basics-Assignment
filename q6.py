# Q6: Grade Calculator

# Taking input
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

# Showing marks
print("Marks:")
print(m1, m2, m3, m4, m5)

# Total
total = m1 + m2 + m3 + m4 + m5
print("Total marks:", total)

# Percentage
percentage = (total / 500) * 100
print("Percentage:", percentage)

# Grade
if percentage >= 90:
    print("Grade: A+ (Outstanding)")
elif percentage >= 80:
    print("Grade: A (Excellent)")
elif percentage >= 70:
    print("Grade: B (Good)")
elif percentage >= 60:
    print("Grade: C (Average)")
elif percentage >= 50:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")

# Pass or Fail
if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")