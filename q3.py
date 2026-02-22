# Q3: String Manipulator


# Logic:
# 1. Take a sentence from user.
# 2. Count total characters (with spaces).
# 3. Remove spaces and count characters.
# 4. Count words using split().
# 5. Convert to uppercase, lowercase and title case.
# 6. Get first and last word.
# 7. Reverse the sentence using slicing.


# Taking input from the user
sentence = input("Enter a sentence: ")

# Display original sentence
print("Original:", sentence)

# Total characters (with spaces)
print("Characters (with spaces):", len(sentence))

# Total characters (without spaces)
without_spaces = sentence.replace(" ", "")
print("Characters (without spaces):", len(without_spaces))

# Total words
words = sentence.split()
print("Words:", len(words))

# Convert to uppercase
print("UPPERCASE:", sentence.upper())

# Convert to lowercase
print("lowercase:", sentence.lower())

# Convert to title case
print("Title Case:", sentence.title())

# First and last word
if len(words) > 0:
    print("First word:", words[0])
    print("Last word:", words[-1])
else:
    print("No words entered.")

# Reverse the sentence
print("Reversed:", sentence[::-1])