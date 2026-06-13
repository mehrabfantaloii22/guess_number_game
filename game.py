import random

number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 3
score = 100  # Starting score

while attempts < max_attempts:
    guess = int(input("Make a guess (number between 1 and 100): "))
    attempts += 1

    if guess < number_to_guess:
        print("The number is higher.")
        score -= 20  # Deduct points for a wrong guess
    elif guess > number_to_guess:
        print("The number is lower.")
        score -= 20  # Deduct points for a wrong guess
    else:
        print("Congratulations! You guessed the correct number.")
        break
else:
    print(f"Sorry! You've used all your attempts. The correct number was {number_to_guess}.")
    
# Final score
print(f"Your final score is: {score}")