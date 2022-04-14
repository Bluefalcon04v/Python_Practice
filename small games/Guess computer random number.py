# guessing computer random number (game)
import random


def guess(x):
    random_number = random.randint(1, x)       # randint() will take random int from range
    guess = 0
    chances_left = 12
    while guess != random_number and chances_left > 0:
        guess = int(input(f"guess a number between 1 to {x}: "))
        chances_left = chances_left - 1
        if guess < random_number:
            print(f"too low, guess again , chances_left: {chances_left}")
        elif guess > random_number:
            print(f"too high, guess again, chances_left: {chances_left}")

    # it will break while loop when we will guess number correctly
    if chances_left == 0:
        print(f"you loose, number was {random_number} ")
    else:
        print(f"congrats! you guessed the number '{random_number}', "
              f"total guesses you made are: {12-chances_left},correctly!!")


guess(1000)
