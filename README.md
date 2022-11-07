# Hangman
The game works by asking the user for an input (letter) and comparing it against the randomly picked word from the list that the user has provided. If the input letter is in the randomly picked word then the user is shown the prompt 'Good guess! {guess} is in the word')'. Followed by the number of lives they have left and also the placement of the guessed letter in the word.

However, if the guessed letter is not correct then the user is promted with 'Sorry, {guess} is not in the word. Try again'. Which results in the user losing a life. The user has a limited number of lives which are set by the user as well. By default the number of lives are set to 5. 

Upon completion of the game the user is congratulated with the promt 'Congratulations. You won the game!' if they win. Otherwise, they are promted with 'You have {num_lives} lives left'. if the number of lives left is zero then 'You lost!' is shown

## Code structure 

- First a class is created. Which is inisialised and has the arguments of the list of words and the number of lives the user has 

- Then a method is created. Which is used to validate if the input the user has provided follows the correct formating. If not then the user is asked to try again with the correct format

- Next method asks the user for an input and checks if the user has already tried the same letter before. If they have then they are asked to provide a unique letter. lastly the user input is passed onto the next method.

- The final method checks to see if the word guessed was correct or not. If it was correct then the user is rewarded and the missing letter(s) from the empty list is revealed, e.g.['b','\_','\_']. However, if the user guesses wrong then they are asked to try again. If the user has used up all their lives. Then they are prompted with 'You lost!'.

- Lastly the class object is created. With the object method being called to start the game.

<div align="center">
To start the game simply run the code and enjoy! 






