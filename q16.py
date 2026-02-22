# Q16: Palindrome Checker

# Palindrome means:
# The word looks the same when we reverse it.
# Example:
# madam -> palindrome
# level -> palindrome
# hello -> not palindrome

# Step 1: Take input from user
word = input("Enter a word: ")

# Step 2: Reverse the word using slicing
reversed_word = word[::-1]

# Step 3: Compare original word and reversed word
if word == reversed_word:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")