import random

secret_number = random.randint(1, 20)

guess = int(input("Guess a number between 1 and 20: "))

if guess == secret_number:
    print("Correct! You win!")
else:
    print("Wrong! The number was:", secret_number)
