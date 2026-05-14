# ---------------------------------------------------------
# QUESTION 5
# Ways to Make Rs.10 Using Coins
# Coins Available : 1, 2, 5, 10
# ---------------------------------------------------------

print("\n========== QUESTION 5 ==========")

count = 0

# Loop through all possible combinations
for one_rupee in range(11):

    for two_rupee in range(6):

        for five_rupee in range(3):

            for ten_rupee in range(2):

                total = (
                    (one_rupee * 1)
                    + (two_rupee * 2)
                    + (five_rupee * 5)
                    + (ten_rupee * 10)
                )

                # Check if total becomes 10
                if total == 10:

                    count += 1

                    print(
                        "1Rs =", one_rupee,
                        ", 2Rs =", two_rupee,
                        ", 5Rs =", five_rupee,
                        ", 10Rs =", ten_rupee
                    )

print("\nTotal Number of Ways :", count)