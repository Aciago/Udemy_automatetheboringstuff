# This is a guess the number game

import random

print('Hello there! What is your name?')
name = input()

print('Hello there, ' + name + ' , I am thinking of a number between 1 and 20. Can you guess which one?')
secretNumber = random.randint(1,20)

for guessesTaken in range (1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #stops loop if guess is not too high or low; it's correct

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '!')
