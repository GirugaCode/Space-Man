import random
import os

guessed_list = []
correct_list = []
attempt_list = []

def load_word():
   words = open('words.txt', 'r')
   words_list = words.readlines()
   words.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word.upper()


def display_guess_list(guessed_list):
    print(' '.join(guessed_list))

def display_attempt_list(attempt_list):
    print('\nLetters attempted')
    print(' '.join(attempt_list))

# Display the beginning of the game
def display_start(secret_word):
    print("""Welcome to Launch the Spaceman!
    You only have (7) wrong attempts to correctly guess the word or else your lover will go to space!
    """)

    print("Your word has: " + str(len(secret_word)) + " letter" +
          ("s" if len(secret_word) > 1 else ""))

# Input error handling
def guess_input():
    try:
        guess = input("\nGuess a letter:\n")
        if len(guess) > 1:
            print("Invalid Guess! Please only input one letter.")
            return guess_input()
        elif not guess.isalpha():
            print("Invalid Guess! Input must be a letter.")
            return guess_input()
        else:
            return guess.upper()
    except (TypeError, ValueError, EOFError):
        print("Invalid input!")
        return guess_input()

# Creates a guess function
def guess(guessed_list):
    guess = guess_input()
    input_letter = False
    attempts = guess in attempt_list
    if guess not in attempt_list:
        attempt_list.append(guess)
    for index, letter in enumerate(correct_list):
        if letter == guess:
            guessed_list[index] = letter
            input_letter = True
    return input_letter or attempts



# Spaceman game function
def spaceman(secret_word):
    os.system('clear')
    display_start(secret_word)

    guessed_list = ["_"] * len(secret_word)

    for letter in secret_word:
        correct_list.append(letter)

    done = False
    wrong_tries = 0


    while not done:
        os.system('clear')
        display_start(secret_word)
        display_guess_list(guessed_list)
        display_attempt_list(attempt_list)
        if wrong_tries > 7:
            print("\nSorry, you have 7 incorrect guesses. The word was", secret_word, ":(")
            print("Game Over")
            done = True
            break

        print("\nNumber of wrong attempts:", wrong_tries)

        found = guess(guessed_list)
        if '_' not in guessed_list:
            done = True
            print("\nCorrect! The word is", secret_word)
            print("You Win!")
        if not found:
            wrong_tries += 1
    input("")


spaceman(load_word())
