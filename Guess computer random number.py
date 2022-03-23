# guessing computer random number (game)
import random


def guess(x):
    random_number = random.randint(1, x)       # randint() will take random int from range
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 to {x}: "))
        if guess < random_number:
            print("too low, guess again ")
        elif guess > random_number:
            print("too high, guess again")         # it will break while loop when we will guess number correctly
    print(f"congrats! you guessed the number '{random_number}' correctly!!")


guess(1000)