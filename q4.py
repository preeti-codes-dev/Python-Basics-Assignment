# Q4: Age Calculator


# Logic:
# 1. Take birth year from user.
# 2. Calculate current age using current year.
# 3. Convert age into months, days, hours and minutes.
# 4. Calculate years left to reach 100.


# Taking birth year from user
birth_year = int(input("Enter your birth year: "))

# Assuming current year is 2025
current_year = 2025

# Calculate age
age = current_year - birth_year

# Display age details
print("Current Age:", age, "years")

# Age in months
months = age * 12
print("Age in months:", months)

# Age in days (approx 365 days per year)
days = age * 365
print("Age in days:", days)

# Age in hours
hours = days * 24
print("Age in hours:", hours)

# Age in minutes
minutes = hours * 60
print("Age in minutes:", minutes)

# Years until 100
years_left = 100 - age
print("Years until age 100:", years_left)