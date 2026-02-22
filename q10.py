# Q10: ATM with Transaction History

# Logic:
# 1. Start the program with an initial balance of ₹10000.
# 2. Create an empty list called history to store all transactions.
# 3. Use a while True loop to continuously show the ATM menu.
# 4. Ask the user to choose an option.

# 5. If user selects "Check Balance":
#    - Display the current balance.

# 6. If user selects "Deposit":
#    - Take deposit amount from user.
#    - Add the amount to balance.
#    - Store the transaction in history list.
#    - Display updated balance.

# 7. If user selects "Withdraw":
#    - Take withdrawal amount from user.
#    - Check if amount is greater than balance.
#      If yes, show "Insufficient balance".
#    - Check if withdrawing will break minimum balance rule (₹500).
#      If yes, show warning message.
#    - Otherwise:
#        * Subtract amount from balance.
#        * Store transaction in history list.
#        * Display updated balance.

# 8. If user selects "Transaction History":
#    - If history list is empty, show message.
#    - Otherwise, print all stored transactions.

# 9. If user selects "Exit":
#    - Display thank you message.
#    - Break the loop to stop program.

# 10. If user enters invalid option:
#     - Show error message.

balance = 10000
history = []

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        history.append("Deposited ₹" + str(amount))
        print("Deposit successful!")
        print("New Balance: ₹", balance)

    elif choice == 3:
        amount = float(input("Enter withdraw amount: "))

        if amount > balance:
            print("Insufficient balance!")

        elif balance - amount < 500:
            print("Minimum balance ₹500 must remain!")

        else:
            balance -= amount
            history.append("Withdrew ₹" + str(amount))
            print("Withdrawal successful!")
            print("New Balance: ₹", balance)

    elif choice == 4:
        print("Transaction History:")
        if len(history) == 0:
            print("No transactions yet.")
        else:
            for item in history:
                print(item)

    elif choice == 5:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice")