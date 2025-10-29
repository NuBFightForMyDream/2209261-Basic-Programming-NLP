"""
File: word_guess.py

Done by : 6730084521 Chatrphol

Title : PA2 Hangman
Course : 2209261 Basic Programming for NLP
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

def play_game(secret_word):
    
    ## Step 1) define status of words , some variables
    guess_word_status = ['-'] * len(secret_word)
    secret_word_list = list(secret_word)
    guess_left = INITIAL_GUESSES
    
    guess_in_condition = False
    guessing_char = ""
    past_guesses = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ## Step 2) Loop until game end
    while guess_left > 0 :
        
        # 2.1) print status
        print(f"The word now looks like this: {''.join(guess_word_status)}")
        
        # 2.2) check guess status
        if guess_left > 1 :
            print(f"You have {guess_left} guesses left.")
        else :
            print(f"You have 1 guess left.")
            
        # 2.3) update past guess status
        if len(past_guesses) > 0 :
            print(f"Your past guesses are {''.join(past_guesses)}")
        
        # 2.4) Input Guessing Char
        guessing_char = input("Type a single letter here, then press enter: ").upper()
        
        ## 2.5) Check if all alphabet is True and in contition that is not pass
        ## If not in condition , always pass
        ## Otherwise , do the game until game end
        
        ## (1) Check Status using for loop
        allCharacterIsAlphabet = True
        for eachChar in guessing_char :
            if eachChar.upper() not in alphabet :
                allCharacterIsAlphabet = False 
                break
         
        ## (2) Check status
        
        if (allCharacterIsAlphabet == False) or (guessing_char == "") :
            pass
    
        elif ((allCharacterIsAlphabet == True) and (len(guessing_char) > 1)) :
            print(f"A guess should be a single character.")
            pass
        
        elif guessing_char in past_guesses :
            pass
        
        else : # game continue
            past_guesses.append(guessing_char)
                
            # 3) check if guessing character in secret_word_list
            if guessing_char in secret_word_list :
                # update to user that guess correct
                print(f"That guess is correct.")
                guess_in_condition = True
            
                # for loop check each each character in word
                for pos in range(len(secret_word_list)) :
                    # if in secret_word_list , replace in guess_word_status with guessing_char
                    if secret_word_list[pos] == guessing_char :
                        guess_word_status[pos] = guessing_char
            
            else : # Guess Wrong
                print(f"There are no {guessing_char}'s in this word")
                # decrease guess by 1
                guess_left -= 1
                
        ## check if win the game
        if guess_word_status == secret_word_list :
            print(f"Congratulations, the word is: {secret_word}")
            break
        
        # print for new line
        print('\n')
        
    ## Step 3) check if lose the game
    if guess_left == 0 and (guess_word_status != secret_word_list) :
        print(f"Sorry, you lost. The secret word was: {secret_word}")

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(121806)
    with open("Lexicon.txt" , "r") as filename :
        lines = filename.readlines()
    return lines[index].strip()

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()