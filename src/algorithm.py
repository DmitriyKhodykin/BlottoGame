"""
Module with the implementation of Blotto Game theory.
"""

import numpy


def blotto_algorithm(user_guess: list) -> [list, str]:
    """
    Compare positions in pairs and calculate the result.
    :return: Computer guess, result message
    """
    # Random computer guess
    random_list = numpy.random.randint(0, 100, 5)
    computer_guess = []
    for i in random_list:
        sum_random = sum(random_list)
        random_choice = int(round(i / sum_random * 100, 0))
        computer_guess.append(random_choice)

    # Count the result
    result = 0
    for i in range(len(user_guess)):
        temp_result = user_guess[i] - computer_guess[i]
        if temp_result < 0:
            result = result + 1
        elif temp_result == 0:
            pass
        elif temp_result > 0:
            result = result - 1

    # Refereeing
    if result > 0:
        result_message = 'You are lose'
    elif result == 0:
        result_message = 'Draw game'
    else:
        result_message = 'You are win'
    return computer_guess, result_message


if __name__ == '__main__':
    blotto_algorithm([22, 22, 22, 20, 14])
