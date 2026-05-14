# ---------------------------------------------------------
# QUESTION 2
# Find Prime Numbers from List
# ---------------------------------------------------------

print("\n========== QUESTION 2 ==========")

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = []

# Loop through each number
for number in numbers:

    # Prime numbers should be greater than 1
    if number > 1:

        is_prime = True

        # Check divisibility
        for i in range(2, number):

            if number % i == 0:
                is_prime = False
                break

        # Add prime number to list
        if is_prime:
            prime_numbers.append(number)

print("Prime Numbers :", prime_numbers)
print("Count of Prime Numbers :", len(prime_numbers))