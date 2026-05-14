"""
Python Program to Find Triplet
Whose Sum is Equal to Given Value
"""

# ---------------------------------------------------
# Given List and Target Value
# ---------------------------------------------------

numbers = [10, 20, 30, 9]
target_value = 59

found = False

# ---------------------------------------------------
# Find Triplets
# ---------------------------------------------------

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        for k in range(j + 1, len(numbers)):

            # Calculate sum of triplet
            total = numbers[i] + numbers[j] + numbers[k]

            # Check condition
            if total == target_value:

                print("Triplet Found :")
                print(numbers[i], numbers[j], numbers[k])

                found = True

# ---------------------------------------------------
# If No Triplet Found
# ---------------------------------------------------

if not found:
    print("No triplet found with sum =", target_value)