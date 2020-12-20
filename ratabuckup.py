"""
File: rota_fortunae.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Game of wheell of forutune.  Users enters word/phrase and solves the word by guessing letters or the complete word/phrase until word/phrase is completed
"""

if __name__ == "__main__":
    usr_game_word = input('What is the word you want the players to guess? ')

    game_word = list(usr_game_word)
    print(game_word)
    hidden_word = []
    used_letters = []

    for character in range(len(game_word)):
        if game_word[character] == ' ':
            hidden_word.append(' ')
        else:
            hidden_word.append('_')

    print(''.join(hidden_word))

    usr_guess = str(input('Guess a letter, or "solve": '))

    while hidden_word != game_word:

        if usr_guess == 'solve':
            usr_solve = list(input('What is the entire puzzle? '))
            if usr_solve == game_word:
                hidden_word = game_word
                print()
            else:
                print('try again')
                usr_guess = input('Guess a letter, or "solve": ')
        elif (len(usr_guess) == 1):# and (usr_guess not in used_letters):

            if (usr_guess in game_word): #and (usr_guess not in used_letters):
                if usr_guess in used_letters:
                    print('you already guessed that')
                else:
                    used_letters.append(usr_guess)
                    for character_index in range(len(game_word)):
                        if game_word[character_index] == usr_guess:
                            hidden_word[character_index] = usr_game_word[character_index]
                print(''.join(hidden_word))
                #usr_guess = str(input('Guess a letter, or "solve": '))

            elif (usr_guess not in used_letters): #and (usr_guess not in game_word):
                if usr_guess in used_letters:
                    print('you already guessed that')
                else:
                    used_letters.append(usr_guess)
                    print("There are no {}'s in the word/phrase".format(usr_guess))
                    print(''.join(hidden_word))
                    #usr_guess = str(input('Guess a letter, or "solve": '))
            else:
                #print('Already used that letter')
                usr_guess = str(input('Guess a letter, or "solve": '))
        """
        else:
            usr_guess = str(input('Guess a letter, or "solve": '))
            print()

        """

    print('You solved the puzzle!')




