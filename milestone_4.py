import random

class hangman:

    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word)) 
        self.guess = str()
        self.word_guessed = ['_','_','_','_','_','_','_'][:len(self.word)]

    def ask_for_input(self):
        list_of_guesses = []
        while self.num_letters > 0 and self.num_lives > 0:
            self.guess = input('Guess a letter: ')
            while len(self.guess) != 1 or self.guess.isalpha() != True:
                self.guess = input('Invalid letter. Please, enter a single alphabetical character').lower()
                
            while self.guess in list_of_guesses:
                self.guess = input('You already tried that letter!')
                while len(self.guess) != 1 or self.guess.isalpha() != True:
                    self.guess = input('Invalid letter. Please, enter a single alphabetical character').lower()               

            list_of_guesses.append(self.guess)
            self.check_guess()

    def check_guess(self):
        if self.guess in self.word:
            print(f'Good guess! {self.guess} is in the word')
            list_values = ([pos for pos, char in enumerate(self.word) if char == self.guess])
            for i in list_values:
                self.word_guessed[i] = self.guess
            print(f'You have {self.num_lives} lives left')
            print(self.word_guessed)
        else:
            print(f'Sorry, {self.guess} is not in the word. Try again')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left')

test = hangman(['apple', 'orange', 'banana', 'grape', 'mango'])

test.ask_for_input()
