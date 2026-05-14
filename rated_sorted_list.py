"""
Python Program to Find the Minimum Element
in a Rotated and Sorted List
"""

# ---------------------------------------------------
# Given Rotated and Sorted List
# ---------------------------------------------------

numbers = [15, 18, 22, 25, 1, 3, 5, 10]

# Assume first element is minimum
minimum = numbers[0]

# ---------------------------------------------------
# Find Minimum Element
# ---------------------------------------------------

for number in numbers:

    # Compare elements
    if number < minimum:
        minimum = number

# ---------------------------------------------------
# Display Result
# ---------------------------------------------------

print("Rotated Sorted List :", numbers)
print("Minimum Element     :", minimum)