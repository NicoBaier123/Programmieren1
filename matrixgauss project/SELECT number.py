import random

random_numbers = [random.randint(1, 49) for _ in range(6)]
SELECT_number = random_numbers

print("Welcome to the number guessing game!")
print("You have 3 tries to guess the 6 numbers.")

for attempt in range(3):
    user_guess = []
    for i in range(6):
        guess = int(input(f"Enter your guess for number {i+1}: "))
        user_guess.append(guess)
    
    if user_guess == SELECT_number:
        print("Congratulations! You guessed all the numbers correctly!")
        break
    else:
        print("Sorry, your guess is incorrect.")
        if attempt < 2:
            print("Please try again.")

print("Game over. The correct numbers were:", SELECT_number)
