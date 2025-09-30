import random
print('Hi! Welcome to a number guessing game! You\'re allowed to choose the range of numbers yourself and have seven attempts to guess the number between this range. Good luck!')

low_bound = int(input('Enter the first number: \n'))
high_bound = int(input('Enter the second number: \n'))

number = random.randint(low_bound, high_bound)

chances = 7
guesses = 0

while guesses < chances:
    guesses += 1
    guess = int(input('Enter your guess: \n'))

    if guesses >= chances and guess != number:
        print(f'You lost! The number was {number}. Better luck next time!')
        break
    if guess == number:
        print(f'Congratulations! You won! The number is {number}')
        break
    if guess > number:
        print('Too high!')
    if guess < number:
        print('Too low!')

