# Q13: Q13 – Statistical Analysis Sum, Average, Median, Mode

# Logic:
# 1. Take numbers from user.
# 2. Calculate sum and average.
# 3. Sort list to find median.
# 4. Use dictionary to find mode.

count = int(input("How many numbers? "))

numbers = []

for i in range(count):
    num = float(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

# Sum
total = 0
for num in numbers:
    total += num

average = total / count

print("\nSum:", total)
print("Average:", average)

# Median
numbers.sort()

if count % 2 == 1:
    median = numbers[count // 2]
else:
    median = (numbers[count // 2 - 1] + numbers[count // 2]) / 2

print("Median:", median)

# Mode
freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
mode = None

for num in freq:
    if freq[num] > max_count:
        max_count = freq[num]
        mode = num

print("Mode:", mode)