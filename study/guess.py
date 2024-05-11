import random
def guess(x):
    number = random.randint(1, x)
    user_guess = 0
    while user_guess != number:
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess < number:
            print("Your guess is too low. Try again.")
        elif user_guess > number:
            print("Your guess is too high. Try again.")      
    print("Congratulations! You guessed the correct number.")
    
guess(20)