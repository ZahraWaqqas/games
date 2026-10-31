#====================================
# Assignment 1, hangman.py
# Name: Zahra Waqqas
# Roll no: 291234050
# Section: A
# Time spent: 16 hours
#====================================

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for x in secret_word: #to loop through each letter in secret_word
        if x not in letters_guessed: #check to see if it is in the letters_guessed
            return False #since that letter is not in secret_word it is not a correct guess, we will return false
    return True #since all letters of secret_word are in letters_guessed so the secret_word has been guessed


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    correct_words = []
    secret_word_list = list(secret_word) #convert to a list so we can compare

    if letters_guessed == []:
        return "*"*len(secret_word_list) #if not letters are guesses then we return string of same length as secret_word

    for x in range(len(secret_word_list)): #to loop through each character of secret_word
        for y in range(len(letters_guessed)): #loop through letters_guessed
            matched_letter = False  # flag to know when it will be correct
            if secret_word_list[x] == letters_guessed[y]: #compare to see if that guessed letter matched the secret word letter
                matched_letter = True  # to flag that that letter is matching
                correct_words.append(secret_word_list[x]) #if they do, it means guesses are correct, then add them to correct_words list
                break #break the current iteration so it doesn't continue unnecessarily, then it will move onto next index of secret_word_list
        if matched_letter==False: #if for the entire x index it doesn't match that means letter isn't in letters_guessed
            correct_words.append('*') #add aestericks to hide that letter since it hasn't been guessed yet
    return "".join(correct_words)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    import string
    all_letters = string.ascii_lowercase #save it in a variable to use
    new = "" #a variable to store new string of letters which still haven't been guessed
    for character in all_letters: #loop through all the letters
        if character not in letters_guessed: #compare to see if there are in the letters_guessed
            new += character #those which aren't will be added to the string
    return new


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply sone guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    number_of_guesses = 10
    letters_guessed = []

    # making helper function for with_help
    def reveal_letters(secret_word, available_letters):
        choose_from = ""  #a string which will have all the words that haven't been guessed yet
        for letter in available_letters:  #loop through each letter in available letters
            if letter in secret_word:  #if that letter is in secret_word and hasn't been guessed yet
                choose_from += letter  #add it to the string
        if choose_from=="":
            return None
        new = random.randint(0, len(choose_from) - 1)
        revealed_letter = choose_from[new]
        return revealed_letter

    # start game
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while number_of_guesses>0:
        print("------")
        print(f"You currently have {number_of_guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guessed_letter = input("Please guess a letter: ").lower()

        if guessed_letter == "!" and with_help==True: # check if with_help can be used
            if number_of_guesses>=3: # makes sure it has enough guesses
                revealed_letter = reveal_letters(secret_word, get_available_letters(letters_guessed)) #if yes then reveal letter using the helper function
                if revealed_letter: #check if letter revealed so it can be added to the guessed letters
                    letters_guessed.append(revealed_letter)
                    number_of_guesses -= 3 #remove 3 guesses as required
                    print(f"Letter revealed: {revealed_letter}")
                    print(get_word_progress(secret_word, letters_guessed))
                else:
                    print(f"Oops! No letters left to reveal: {get_word_progress(secret_word, letters_guessed)}")
            else:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}") #since not enough guesses we print message

        if not guessed_letter.isalpha() or len(guessed_letter)>1 or len(guessed_letter)<1: #to ensure it is a letter and not some other character. And that is not a string
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
            continue

        if guessed_letter in letters_guessed: #to ensure that that letter has not already been guessed
            print(f"Oops! You’ve already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            continue

        letters_guessed.append(guessed_letter) #now add the guess

        if guessed_letter in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        elif guessed_letter in "aeiou":
            number_of_guesses-=2
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
        else:
            number_of_guesses-=1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        score = (number_of_guesses + (4*len(set(secret_word))) + (3*len(secret_word)))
        print(f"Your total score for this game is: {score}")
        return
    if not has_player_won(secret_word, letters_guessed):
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, True)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your assignment. However, please run test_a1_student.py
    # one more time before submitting to make sure all the tests pass.


