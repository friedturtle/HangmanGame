import random
import sys
import time

words_list = "C:\\Users\\Brendan\\PycharmProjects\\HangmanGame\\wordslist.txt"
WORDS = open(words_list).read().splitlines()

WORDS = [element.upper() for element in WORDS]

def newword():
    '''Generate a new word'''
    word = random.choice(WORDS)
    print(word)
    wordlength = len(word)
    print(wordlength)
    #Generate letter list
    letters = list(word)
    print(letters)
    return word


'''Split word into letters'''




    #Determine if letter guessed before

'''Allow user to guess a letter pass fail'''

def guessword(word):
    #Allow the user to guess the entire word
    guess = word

def main():
    endgame = False

    while not endgame:
        lives = 9
        win = 0
        print("Welcome to Hangman!")
        print("You start with", lives, "lives")
        #Generate Word
        word = newword()
        word_length = len(word)
        print("Word chosen. Word is", word_length, "letters long. \n")
        #Set secret and eliminated letters list
        secret = []
        eliminated = []
        #Generate secret list
        for i in range (0, word_length):
            secret.append('*')
        print(secret)
        #Ask the user to guess
        while lives:
            oldletter = 1
            while oldletter:
                myguess = input("Guess a letter! : ").upper()
                if myguess not in eliminated:
                    oldletter = 0
                elif myguess in eliminated:
                    print("Already guessed this letter. Try again!")
            hit = 0
            for i in range(0, len(word)):
                if myguess == word[i]:
                    hit += 1
                    secret[i] = word[i]
            if not hit:
                print("Bad luck!", lives-1, "lives remaining.")
                lives -= 1
                if lives == 0:
                    retry = input("Out of lives! Press y to play again.: ")
                    if retry != "y":
                        endgame = True
            else:
                print("Correct! Word is: ", secret)
            eliminated.append(myguess)
            print("Eliminated: ", eliminated)
            if ''.join(secret) == word:
                win = 1
                retry = input("You win! Press y to play again.: ")
                if retry != "y":
                    print("Exiting...")
                    sys.exit()
                else:
                    lives = 0

















main()
