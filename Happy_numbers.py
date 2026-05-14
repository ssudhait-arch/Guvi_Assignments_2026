print("\n========== QUESTION 3 ==========")

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy_number(number):
    """
    Function to check whether a number is happy or not.
    """

    visited_numbers = set()

    while number != 1 and number not in visited_numbers:

        visited_numbers.add(number)

        total = 0

        # Find sum of square of digits
        while number > 0:
            digit = number % 10
            total += digit ** 2
            number = number // 10

        number = total

    return number == 1


happy_numbers = []

# Check each number in list
for number in numbers:

    if is_happy_number(number):
        happy_numbers.append(number)

print("Happy Numbers :", happy_numbers)
print("Count of Happy Numbers :", len(happy_numbers))
