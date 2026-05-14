"""
Program to Find Duplicate Elements
from Three Python Lists
"""

# ---------------------------------------------------
# Create Three Lists
# ---------------------------------------------------

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 70, 80, 90]
list3 = [20, 30, 40, 100]

# Empty list to store duplicates
duplicates = []

# ---------------------------------------------------
# Find Common Elements
# ---------------------------------------------------

for number in list1:

    # Check whether number exists in all lists
    if number in list2 and number in list3:

        duplicates.append(number)

# ---------------------------------------------------
# Display Output
# ---------------------------------------------------

print("List 1 :", list1)
print("List 2 :", list2)
print("List 3 :", list3)

print("\nDuplicate Elements in all three lists:")
print(duplicates)