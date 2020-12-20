"""
File: rota_fortunae.py
Author: Jason Song
Date: 10/04/2020
Lab Section: 22
Email: jason20@umbc.edu
Description: Game of wheel of fortune.  Users enters word/phrase and solves the word by guessing letters or the complete word/phrase until word/phrase is completed
"""

if __name__ == "__main__":
    usr_game_word = input('What is the word you want the players to guess? ')

    game_word = list(usr_game_word.lower())
    hidden_word = []
    used_letters = []

    for character in range(len(game_word)):
        if game_word[character] == ' ':
            hidden_word.append(' ')
        else:
            hidden_word.append('_')

    print(''.join(hidden_word))

    usr_guess = str(input('Guess a letter, or "solve": '))


    while hidden_word != list(usr_game_word):   #while loop exit condition once user has completed puzzle by matching the word of the start of the game
        if usr_guess == 'solve':    #checks condition if user inputs command to guess the word/phrase in it's entirety win the game
            usr_solve = list(input('What is the entire puzzle? ').lower())
            if usr_solve == game_word:
                hidden_word = game_word

            else:
                print('try again')
                usr_guess = input('Guess a letter, or "solve": ')
        elif (len(usr_guess) == 1): #condition runs only if letter is inputted to start check if letter is in word

            if (usr_guess in game_word) and (usr_guess not in used_letters):    #check to see if letter is in the hidden word but only if letter hasn't been used yet to avoid redundancy
                used_letters.append(usr_guess)
                for character_index in range(len(game_word)):   #for loop to iterate through every letter in word/phrase and replace every 'blank' spot in hidden word with letter matching the user input
                    if game_word[character_index] == usr_guess:
                        hidden_word[character_index] = usr_game_word[character_index]
                print(''.join(hidden_word))

            elif usr_guess not in game_word:    #condition for if the user input letter is not in the hidden word
                if usr_guess in used_letters:   #checks to see if letter has been used already
                    print("You have guessed that letter before, but it's still not in the word.")
                    print(''.join(hidden_word))
                    usr_guess = str(input('Guess a letter, or "solve": ').lower())
                else:   #if letter hasn't been used it will default to adding it to the list of used letters then outputting message to let player know it is not in word.
                    used_letters.append(usr_guess)
                    print("There are no {}'s in the word/phrase".format(usr_guess))
                    print(''.join(hidden_word))
                    usr_guess = str(input('Guess a letter, or "solve": ').lower())

            else:
                usr_guess = str(input('Guess a letter, or "solve": ').lower())
        elif len(usr_guess) > 1:    #condition if user input has length of letters > 1
            print('Please enter a letter')
            usr_guess = str(input('Guess a letter, or "solve": ').lower())


    print('You solved the puzzle!')