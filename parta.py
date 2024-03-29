import matplotlib.pyplot as plt
from fractions import Fraction

def main():
    # Initialize memoization table
    memo = [0] * 13

    diceA = [1, 2, 3, 4, 5, 6]
    diceB = [1, 2, 3, 4, 5, 6]

    # Populate memoization table
    for i in diceA:
        for j in diceB:
            memo[i + j] += 1

    # QUESTION 1 : Print count of possible combinations
    print("---------------------------------------------------------------Count of possible combinations: 36 -----------------------------------------------------------------------------------------------------------------------------------------------------------")

    # QUESTION 2 : Print all possible combinations
    print("All the possible combinations are:")
    for i in range(1, 7):
        for j in range(1, 7):
            print("(", i, ",", j, ")", end=" ")
        print()
    print("----------------------------------------------------------------------")

    # QUESTION 3 : Calculate the Probability of all Possible Sums
    print("Sum\t\tProbability(Fraction)\tProbability (Decimal)-------------------------------------------------------------------------------------------------")
    for i in range(2, 13):
        probability_fraction = Fraction(memo[i], 36)
        probability_decimal = memo[i] / 36
        print(f"{i}\t\t{memo[i]}/36 = {probability_fraction}\t{probability_decimal:.2f}")
    print()

    # Plotting
    x = list(range(2, 13))
    y = [memo[i] / 36 for i in range(2, 13)]

    plt.bar(x, y, color='skyblue')

    for i, probability in enumerate(y):
        plt.text(x[i], probability, f'{probability:.2f}', ha='center', va='bottom')

    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Dice Sums')
    plt.xticks(x)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
