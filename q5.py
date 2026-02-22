# Q5: Bill Splitter


# Logic:
# 1. Take total bill, number of people, tax and tip percentage.
# 2. Calculate tax amount.
# 3. Add tax to subtotal.
# 4. Calculate tip on taxed amount.
# 5. Divide final bill equally among people.



# Taking input from user
total_bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

# Calculating tax
tax_amount = total_bill * tax_percent / 100
after_tax = total_bill + tax_amount

# Calculating tip
tip_amount = after_tax * tip_percent / 100
final_total = after_tax + tip_amount

# Amount per person
per_person = final_total / people

# Printing results
print("=== BILL BREAKDOWN ===")
print("Subtotal: ₹",total_bill)
print("Tax: ₹",tax_amount)
print("After tax: ₹",after_tax)
print("Tip: ₹",tip_amount)
print("Total: ₹",final_total)
print("Per person: ₹",per_person)