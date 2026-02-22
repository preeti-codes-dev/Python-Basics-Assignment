# Q19: Text Analysis

# Logic:
# 1. Take text from user.
# 2. Count words using split().
# 3. Count vowels and consonants using loop.
# 4. Reverse text using slicing.
# 5. Check palindrome.
# 6. Remove vowels.
# 7. Find longest word.
# 8. Count word frequency.

text = input("Enter text: ")

print("=== TEXT ANALYSIS ===")

# Count words
words = text.split()
print("Words:", len(words))

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Reverse text
print("Reversed:", text[::-1])

# Palindrome check
cleaned = text.lower().replace(" ", "")
if cleaned == cleaned[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

# Remove vowels
no_vowels = ""
for ch in text:
    if ch not in vowels:
        no_vowels += ch

print("Without vowels:", no_vowels)

# Longest word
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest, "(" + str(len(longest)) + " letters)")

# Word frequency
freq = {}
for word in words:
    word = word.lower()
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:", end=" ")

first = True
for word in freq:
    if not first:
        print(", ", end="")
    print(word + ": " + str(freq[word]), end="")
    first = False