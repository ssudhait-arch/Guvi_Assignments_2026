"""
Python Assignment Programs
Author : Your Name

This file contains solutions for:
1. Even and Odd Numbers
2. Prime Numbers
3. Happy Numbers
4. Sum of First and Last Digit
5. Coin Combination Problem
"""

# ---------------------------------------------------------
# QUESTION 1
# Separate Even and Odd Numbers from List
# ---------------------------------------------------------

print("\n========== QUESTION 1 ==========")

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []
odd_numbers = []

# Loop through list
for number in numbers:

    # Check even numbers
    if number % 2 == 0:
        even_numbers.append(number)

    # Check odd numbers
    else:
        odd_numbers.append(number)

print("Original List :", numbers)
print("Even Numbers  :", even_numbers)
print("Odd Numbers   :", odd_numbers)
