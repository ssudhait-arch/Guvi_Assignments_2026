
# ---------------------------------------------------------
# QUESTION 4
# Sum of First and Last Digit
# ---------------------------------------------------------

print("\n========== QUESTION 4 ==========")


# Get input from user
number = input("Enter an integer: ")

# Remove negative sign if present
number = number.replace("-", "")

# First digit
first_digit = int(number[0])

# Last digit
last_digit = int(number[-1])

# Sum
total = first_digit + last_digit

print("First Digit :", first_digit)
print("Last Digit  :", last_digit)
print("Sum         :", total)
