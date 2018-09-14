import random
import os

correct_list = []
guessed_list = []
attempt_list = []

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word


def display_guess_list(guessed_list):
    print(' '.join(guessed_list))

def display_attempt_list(attempt_list):
    print('\nLetters attempted')
    print(' '.join(attempt_list))

# Input error handling
def guess_input():
    try:
        guess = input("Guess a letter:")
        if len(guess) > 1:
            print("Invalid input! Please enter only one letter.")
            return guess_input()
        elif guess.isalpha():
            print("Invalid input! Please enter a letter.")
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
        attempt.append(guess)
    for index, letter in enumerate(correct_list):
        if letter == guess:
            attempt_list[index] = letter
            input_letter = True
    return input_letter or attempts

# Display the beginning of the game
def display_start(secret_word):
    print("""Welcome to Spaceman!
    You only have seven (7) wrong attempts to correctly guess the word or else non-spaceman go to space!
    """)
    
    print("Your word has: " + str(len(secret_word)) + " letter" +
          ("s" if len(secret_word) > 1 else ""))

### def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#
#     # FILL IN YOUR CODE HERE...
#
#
# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: string, of letters and underscores.  For letters in the word that the user has
#     guessed correctly, the string should contain the letter at the correct position.  For letters
#     in the word that the user has not yet guessed, shown an _ (underscore) instead.
#     '''
#     # FILL IN YOUR CODE HERE...
#
#
#
#
# def get_available_letters(letters_guessed):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#
#
#
#
# def spaceman(secret_word):
#     '''
#     secretWord: string, the secret word to guess.
#     Starts up a game of Spaceman in the command line.
#     * At the start of the game, let the user know how many
#       letters the secretWord contains.
#     * Ask the user to guess one letter per round.
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#     '''
#     # FILL IN YOUR CODE HERE...

    # At the start of the game, let the user know how many
    #   letters the secretWord contains.



#
# secret_word = load_word()
# spaceman(load_word())
