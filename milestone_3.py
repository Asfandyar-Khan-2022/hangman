secret_word = 'apple'

def ask_for_input():
    guess = input('Guess a letter: ')
    while len(guess) != 1 or guess.isalpha() != True:
        guess = input('Please only write a single letter: ').lower()
    return guess

def check_guess(guess):
    if guess in secret_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

check_guess(ask_for_input())

# newer changes 