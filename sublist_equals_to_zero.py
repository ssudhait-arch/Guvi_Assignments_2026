"""
Python Program to Find Whether
a Sublist with Sum Equal to Zero Exists
"""

# ---------------------------------------------------
# Given List
# ---------------------------------------------------

numbers = [4, 2, -3, 1, 6]

found = False

# ---------------------------------------------------
# Check All Possible Sublists
# ---------------------------------------------------

for i in range(len(numbers)):

    current_sum = 0

    for j in range(i, len(numbers)):

        # Add elements one by one
        current_sum += numbers[j]

        # Check if sum becomes zero
        if current_sum == 0:

            print("Sublist with sum zero found:")
            print(numbers[i:j + 1])

            found = True
            break

    if found:
        break

# ---------------------------------------------------
# If No Sublist Found
# ---------------------------------------------------

if not found:
    print("No sublist with sum zero exists.")