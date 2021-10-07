"""
Module with the implementation of Blotto Game theory.
"""
import numpy


def blotto_algorithm(user_guess: list):
    """
    Compare positions in pairs and calculate the result.
    :return: None
    """
    computer = [20, 20, 17, 21, 22]  # AI
    c1 = numpy.random.normal(20, 5, 5)
    c1 = numpy.round(c1, 0)

    print("human:", user_guess, "SUM:", sum(user_guess))
    print("computer:", c1, "SUM:", sum(c1))

    res = 0
    for i in range(len(user_guess)):
        r = user_guess[i] - computer[i]
        if r < 0:
            res = res + 1
        elif r == 0:
            pass
        elif r > 0:
            res = res - 1

    print("RES:", res)

    if res > 0:
        print("You are lose")
    elif res == 0:
        print("Draw game")
    else:
        print("You are win")


if __name__ == '__main__':
    blotto_algorithm([20, 20, 20, 20, 20])
