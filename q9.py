# Q9: Ticket Pricing System


# Logic:
# 1. Take age, day and number of tickets.
# 2. Decide base price using age.
# 3. Check weekend discount (20%).
# 4. Calculate total amount.


# Taking inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ")
tickets = int(input("Enter number of tickets: "))

# Age-based pricing
if age < 3:
    base_price = 0
elif age >= 3 and age <= 12:
    base_price = 150
elif age >= 13 and age <= 59:
    base_price = 300
else:
    base_price = 200

# Total before discount
total = base_price * tickets

# Day-based discount
if day.lower() == "friday" or day.lower() == "saturday" or day.lower() == "sunday":
    discount = total * 0.20
else:
    discount = 0

# Final amount after discount
final_amount = total - discount

# Display results
print("\nBase price per ticket: ₹", base_price)
print("Total before discount: ₹", total)
print("Discount: ₹", discount)
print("Final amount to pay: ₹", final_amount)