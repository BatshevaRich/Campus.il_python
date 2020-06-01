import random
import string
import os
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""

HANGMAN_PHOTOS = {'1': """
    x-------x""",
                  '2': """
    x-------x
    |
    |
    |
    |
    |""",
                  '3': """
    x-------x
    |       |
    |       0
    |
    |
    |
""",
                  '4': """
    x-------x
    |       |
    |       0
    |       |
    |
    |
""",
                  '5': """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
                  '6': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
                  '7': """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}

MAX_TRIES = 6

def check_win(secret_word, old_letters_guessed):
    """checks if all letters of secret word are in list of guessed letters

    Arguments:
        secret_word {string} the secret word
        old_letters_guessed {list} list of all letters guessed

    Returns: true if all letters are in list, otherwise false
       return type: bool
    """
    mapped = show_hidden_word(secret_word, old_letters_guessed)
    if '_' in mapped:
        return (False, ' '.join(mapped))
    return (True, ' '.join(mapped))

def is_valid_input(letter_guessed):
    """func to return if the input is valid, by the rules of hangman

    Arguments:
        letter_guessed {char} -- input from user

    Returns:
        bool -- true if valid, false otherwise
    """
    if len(letter_guessed) > 1:
        if letter_guessed not in string.ascii_lowercase:
            return False
        else:
            return False
    elif letter_guessed not in string.ascii_lowercase:
        return False
    return True

def check_valid_input(letter_guessed, old_letters_guessed):
    """checks if letter is valid- if user did not guess the letter and letter complies
    to rules of hangman

    Arguments:
        letter_guessed {char} -- input from user
        old_letters_guessed {list} -- letters user guessed already

    Returns:
        bool -- true if valid, false otherwise.
    """
    if is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed:
        return True
    return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed: list):
    """updates letter if correct and adds it to list of old letters.
    otherwise prints letters guessed on screen to remind user.

    Arguments:
        letter_guessed {string} -- input from user
        old_letters_guessed {list} -- list of letters guessed

    Returns:
        bool -- return true if valid, false otherwise and prints help for user on screen.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print('X')
    print('->'.join(old_letters_guessed))
    return False

def findOccurrences(secret_word, current_letter):
    """helper func, finds all occurences of current letter in the secret word

    Arguments:
        secret_word {string} -- the secret word
        current_letter {char} -- current letter from the list of old letters

    Returns:
        list -- list of indexes in list of old letters where current letter appears
    """
    return [i for i, letter in enumerate(secret_word) if letter == current_letter]

def show_hidden_word(secret_word, old_letters_guessed):
    """displays the hidden word according to the old letters guessed, with _ if the letter has not been guessed.

    Arguments:
        secret_word {string} -- the secret word
        old_letters_guessed {list} -- list of all letters guessed

    Returns:
        string -- return the hidden word with _ where user has not guessed the word
    """
    mapped = list('_' * len(secret_word))
    for element in old_letters_guessed:
        for index in findOccurrences(secret_word, element):
            mapped[index] = element
    return mapped

def choose_word(file_path, index):
    """func to choose word from user file, and word index given by user

    Arguments:
        file_path {string} -- path to file
        index {int} -- index of word

    Returns:
        string -- the secret word
    """
    if not os.path.isfile(file_path):
        return False
    words_file = open(file_path, 'r')
    words =  words_file.read()
    words = [''.join(w for w in word if w.isalpha()) for word in words.split()]
    words_file.close()
    unique_words = []
    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)
    word_to_guess = ''
    if index >= len(words):
        word_to_guess = words[index % len(words) - 1]
    else:
        word_to_guess = words[index]
    # return (len(unique_words), word_to_guess)
    return word_to_guess

def begin_game():
    """func for start of game actions, prints screen saver and gets file from user

    Returns:
        string -- the word
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)
    the_word = False
    while the_word == False:
        the_word = choose_word(input('enter file path '), int(input('enter index ')))
    print("let's start!")
    print(HANGMAN_PHOTOS[str(1)])
    print('_ ' * len(the_word))
    return the_word

def main():
    old_letters_guessed = []
    the_word = begin_game()
    num_of_tries = 1
    old_letters_status_before_update = []
    while num_of_tries <= MAX_TRIES:
        guess = input("guess a letter! ")
        updated = try_update_letter_guessed(guess, old_letters_guessed)
        mapped = check_win(the_word, old_letters_guessed)
        if mapped[0] == True and updated == True:
            print(mapped[1])
            print('WIN')
            break
        elif updated == False:
            continue
        elif mapped[0] == False:
            if guess not in the_word and guess not in old_letters_status_before_update:
                old_letters_status_before_update = list(old_letters_guessed)
                num_of_tries += 1
                print(':(')
                print(HANGMAN_PHOTOS[str(num_of_tries)])
            print(mapped[1])
    if num_of_tries > MAX_TRIES:
        print('LOSE')

if __name__ == "__main__":
    main()
