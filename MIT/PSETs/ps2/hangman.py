import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    answer = 1
    for char in secret_word:
        if char in letters_guessed:
            answer = answer * 1
        else:
            answer = answer * 0
    return True if answer > 0 else False


def get_guessed_word(secret_word, letters_guessed):
    # which letters in secret_word have been guessed so far.

    answer = []
    for char in secret_word:
        if char in letters_guessed:
            answer.append(char)
        else:
            answer.append('_ ')
    return ''.join(answer)


def get_available_letters(letters_guessed):
    # which letters have not yet been guessed.

    answer = list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in answer:
            answer.remove(char)
    return ''.join(answer)


def input_checker(letters_guessed):
    while letters_guessed not in string.ascii_letters or len(letters_guessed) != 1:
        print('Invalid input!')
        letters_guessed = input('Please guess a letter: ').lower()
    return letters_guessed


def hangman(secret_word):
    number_of_guesses = 6

    print('Welcome to the game Hangman! \nI am thinking of a word that is', len(secret_word), 'letters long')
    print(get_guessed_word(secret_word, ''), '\nYou have', number_of_guesses, 'guesses left.')
    print('Available letters:', get_available_letters(''))

    letters_guessed = input('Please guess a letter: ').lower()
    input_checker(letters_guessed)

    if letters_guessed in secret_word:
        print('Good guess:  ', get_guessed_word(secret_word, letters_guessed))
    else:
        number_of_guesses -= 1
        print('Wrong guess! Try again!:  ', get_guessed_word(secret_word, letters_guessed))

    print('~~~~~~~~~~~~~~~~~~~~~~~~', '\nYou have', number_of_guesses, 'guesses left.')
    print('Available letters:', get_available_letters(letters_guessed))

    while not is_word_guessed(secret_word, letters_guessed) and number_of_guesses > 0:

        new_input = input('Please guess a letter: ').lower()
        input_checker(new_input)

        if new_input in letters_guessed:
            print('You have already guessed that letter.')
        elif new_input in secret_word:
            letters_guessed += new_input
            print('Good guess:  ', get_guessed_word(secret_word, letters_guessed))
        else:
            number_of_guesses -= 1
            letters_guessed += new_input
            print('Wrong guess! Try again!:  ', get_guessed_word(secret_word, letters_guessed))

        if number_of_guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break
        elif is_word_guessed(secret_word, letters_guessed):
            print('Congratulations, you won!')
            break
        print('~~~~~~~~~~~~~~~~~~~~~~~~', '\nYou have', number_of_guesses, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)
