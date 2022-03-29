import random
from words import words
import string


def get_word(words):            # to check if words doesn't have any blanks or dash in it.
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)       # letters to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()             # already used letters

    # getting user inputs
    while len(word_letters) > 0:
        print('you have already used these letters: ', ' '.join(used_letters))
        # for presentation.
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word: ', ' '.join(word_list))

        used_letter = input('guess a letter: ').upper()
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)

        elif used_letter in used_letters:
            print("already used character ")

        else:
            print("invalid character ")

    print(f"YAY!, YOU GUESSED THE {word} CORRECTLY")


hangman()
