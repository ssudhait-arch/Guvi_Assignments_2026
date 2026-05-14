"""
Python Program to Find the First Non-Repeating Element
in a Given List of Integers
"""

# ---------------------------------------------------
# Given List
# ---------------------------------------------------

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Variable to store first non-repeating element
first_non_repeating = None

# ---------------------------------------------------
# Find Non-Repeating Element
# ---------------------------------------------------

for number in numbers:

    # Count occurrence of each number
    if numbers.count(number) == 1:

        first_non_repeating = number
        break

# ---------------------------------------------------
# Display Result
# ---------------------------------------------------

print("Given List :", numbers)

if first_non_repeating is not None:
    print("First Non-Repeating Element :", first_non_repeating)

else:
    print("No non-repeating element found.")