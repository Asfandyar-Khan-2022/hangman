import random

class hangman:                                                      

    def __init__(self, word_list, num_lives = 5):                                                           # default the number of lives as 5
        self.word = random.choice(word_list)                                                                # pick a random number
        self.num_lives = num_lives                                                                          
        self.num_letters = len(set(self.word))                                                              # number of all unique characters    
        self.guess = str()
        self.word_guessed = []
        for i in range (len(self.word)):                                                                    # create a list that consists of the same number of underscore as the letters in the word
            self.word_guessed += '_'
    
    def valid_letter(self):                                                                                 # function to check if the input is a valid character
        while len(self.guess) != 1 or self.guess.isalpha() != True:
            self.guess = input('Invalid letter. Please, enter a single alphabetical character').lower()

    def ask_for_input(self):                                                                                # this function starts the game by asking for an input
        list_of_guesses = []

        while self.num_letters > 0 and self.num_lives > 0:                                                  # while the game has not ended. Ask for a guess
            self.guess = input('Guess a letter: ')                                                          
            self.valid_letter()

            while self.guess in list_of_guesses:                                                            # if a letter has been tried then ask them to try again
                self.guess = input('You already tried that letter!')
                self.valid_letter()                                                                         

            list_of_guesses.append(self.guess)                                                              # if a word has been guessed then is should be saved to comparison
            self.check_guess()

    def check_guess(self):                                                                                  # function used to check if the word guessed is correct or not
        if self.guess in self.word:                                                                         # if the guessed letter is in the word. Then display the results
            print(f'Good guess! {self.guess} is in the word')
            list_values = ([pos for pos, char in enumerate(self.word) if char == self.guess])
            for i in list_values:
                self.word_guessed[i] = self.guess
            print(f'You have {self.num_lives} lives left')
            print(self.word_guessed)
            self.num_letters -= 1                                                                           # remove the number of words left to guess
            if self.num_letters == 0:
                print ('Congratulations. You won the game!')
        else:
            print(f'Sorry, {self.guess} is not in the word. Try again')                                     # if the guess is wrong then update the number of lives
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left')
            if self.num_lives == 0:
                print('You lost!')

game = hangman(['apple', 'orange', 'banana', 'grape', 'mango'], 5)                                          # instantiate then pass the word list parameters and number of lives as input
game.ask_for_input()                                                                                        # start the game
