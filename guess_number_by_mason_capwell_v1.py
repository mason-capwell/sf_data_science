"""guess the hidden number.
The computer itself guesses and guesses the number itself
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly guess a number

    Args:
        number (int, optional): Hidden random number. Defaults to 1.

    Returns:
        int: Numbers of attempts
    """
    # initial number of attempts
    count = 0
    # the minimum and maximum value of the limits in the interval
    mn, mx = 1, 100
    # random number
    predict = np.random.randint(1, 100)

    # set conditions for finding a random number by pc
    while number != predict:
        count += 1

        if number > predict:
            mn = predict + 1
            predict = (mx + mn) // 2
        elif number < predict:
            mx = predict - 1
            predict = (mx + mn) // 2
    # return the number of attempts
    return count


def score_game(random_predict) -> int:
    """For what number of attempts on average for 1000 approaches our algorithm guesses

    Args:
        random_predict ([type]): number guessing function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    # fix seed for reproducibility
    np.random.seed(1)
    # guessed numbers for 1000 passes
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in: {score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
