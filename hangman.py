# HANGMAN

from colorama import Fore, init
from cls import cls
from nltk.corpus import words
import random
import json

cls()
init()

none = """
    _____
   |  |
   |  
   |
   |
   |
-------
"""
head = """
    _____
   |  |
   |  o
   |
   |
   |
-------
"""
body = """
    _____
   |  |
   |  o
   |  |
   |
   |
-------
"""
leftarm = """
    _____
   |  |
   |  o
   | /|
   |
   |
-------
"""
rightarm = """
    _____
   |  |
   |  o
   | /|\\
   |
   |
-------
"""
leftleg = """
    _____
   |  |
   |  o
   | /|\\
   | /
   |
-------
"""
done = """
    _____
   |  |
   |  o
   | /|\\
   | / \\
   |
-------
"""

# easy = [word.lower() for word in words.words() if 3 <= len(word) <= 5]
# medium = [word.lower() for word in words.words() if 6 <= len(word) <= 7]
# hard = [word.lower() for word in words.words() if 8 <= len(word) <= 9]
# impossible = [word.lower() for word in words.words() if len(word) > 9]

with open('./WORD/easy.json') as f:
    easyd = json.load(f)
with open('./WORD/medium.json') as f:
    medd = json.load(f)
with open('./WORD/hard.json') as f:
    hardd = json.load(f)
with open('./WORD/impossible.json') as f:
    impd = json.load(f)

easy = easyd
medium = medd
hard = hardd
impossible = impd

blank = ' '
underscore = '_'

def start():
    global difficulty

    cls()
    print('What difficulty do you want to play on?')
    print(Fore.GREEN + f'(1) [3-5 Letters]{blank*5}' + Fore.YELLOW + f'(2) [6-7 Letters]{blank*5}' + Fore.LIGHTRED_EX + f'(3) [8-9 Letters]{blank*5}' + Fore.RED + f'(4) [>9 Letters]{blank*5}' + Fore.RESET + '(0) Exit')

    diff = input('> ')

    if diff == str(0):
        cls()
        exit()
    elif diff == str(1):
        print(Fore.GREEN + 'Easy Mode')
        difficulty = 'easy'
    elif diff == str(2):
        print(Fore.YELLOW + 'Medium Mode')
        difficulty = 'medium'
    elif diff == str(3):
        print(Fore.LIGHTRED_EX + 'Hard Mode')
        difficulty = 'hard'
    elif diff == str(4):
        print(Fore.RED + 'Impossible Mode')
        difficulty = 'impossible'
    else:
        cls()
        print(Fore.YELLOW + 'Please input "1", "2", "3", "4" or "0"' + Fore.RESET)
        input('Press any key to continue: ')
        cls()
        exit()

    cls()
    game()

def game():
    print(Fore.RESET)

    wrong = []
    iguesses = 0

    if difficulty == 'easy':
        word = random.choice(easy)
    elif difficulty == 'medium':
        word = random.choice(medium)
    elif difficulty == 'hard':
        word = random.choice(hard)
    elif difficulty == 'impossible':
        word = random.choice(impossible)

    rword = '_' * len(word)

    while iguesses < 6:
        print(rword)
        print()
        print('Input a letter:')
        guess = input('> ')
        print()

        if guess not in word and guess not in wrong:
            wrong.append(guess)
            iguesses += 1

            if iguesses == 1:
                cls()
                print(head)
            if iguesses == 2:
                cls()
                print(body)
            if iguesses == 3:
                cls()
                print(leftarm)
            if iguesses == 4:
                cls()
                print(rightarm)
            if iguesses == 5:
                cls()
                print(leftleg)
            if iguesses == 6:
                cls()
                print(done)

        elif guess in word:
            if iguesses == 0:
                cls()
                print(none)
            if iguesses == 1:
                cls()
                print(head)
            if iguesses == 2:
                cls()
                print(body)
            if iguesses == 3:
                cls()
                print(leftarm)
            if iguesses == 4:
                cls()
                print(rightarm)
            if iguesses == 5:
                cls()
                print(leftleg)
            if iguesses == 6:
                cls()
                print(done)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                rword = rword[:index] + guess + rword[index + 1:]

        print()

        for guess in wrong:
            print(f'{guess}')
        
        print()

        if rword == word:
            print('You win!')
            break
    print(word)

if __name__ == '__main__':
    start()