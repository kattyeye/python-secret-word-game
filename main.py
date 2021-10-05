# player gets 7 incorrect guesses
# don't let player guess same char more than 2 times

# _ _ _ _ _
# input
# response

# _ e _ _ _

# loop that keeps firing, if they guess the word kick them out

import random

words_list = ['cat', 'rat', 'mouse', 'grasshopper', 'tangerine',
'dragon', 'donkey', 'shrek', 'pie', 'muffin', 'dog']

word = random.choice(words_list)

print("Guess the letters. ")
print('You may guess more than one letter, if you think you know the word.')

guesses = ''


turns = 7

while turns > 0:
    failed_attempts = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed_attempts += 1

    if failed_attempts == 0:
        print("Yay! You win!")
        print("The word is: ", word)
        break

    guess = input("Guess a letter: ")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong.")
        print("You have", + turns, "more guesses.")


        if turns == 0:
            print("You lose :(")