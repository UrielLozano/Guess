#Guess the Number Game
import random
print('Hello. What is your name?')
name = input()

print(name + ', guess a number between 1-50 in 7 tries')
secretNumber = random.randint(1, 50)
print ('Take a guess')
for guessTaken in range(7):
    guess = int(input())
    if guess < secretNumber:
        print('Guess is too low')
    elif guess > secretNumber:
        print('Guess is too high')
    else:
        break
if guess == secretNumber:
    print(name + ', you guessed correct.Yay')
else:
    print('You took too many guesses. The correct number is ' + str(secretNumber))
