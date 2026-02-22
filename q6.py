# Q6: Grade Calculator


# Logic:
# 1. Take marks for 5 subjects.
# 2. Calculate total and percentage.
# 3. Assign grade based on percentage.
# 4. Check if all subjects are >= 40 for pass.



# Taking marks input
m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

# Display marks
print("\nMarks Entered:")
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Subject 4:", m4)
print("Subject 5:", m5)

# Calculate total
total = m1 + m2 + m3 + m4 + m5
print("\nTotal marks (out of 500):", total)

# Calculate percentage
percentage = (total / 500) * 100
print("Percentage:", percentage)

# Grade calculation
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

# Pass or Fail condition
if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")