import random

def generate_number():
    num = random.randint(1, 5)
    return num

def take_number():
    guess = input("I'm thinking of a number! Try to guess the number I'm thinking of: ")
    guess = int(guess)
    return guess

def check_number(guess, num):
    while True:
        if guess < num:
            guess = int(input("Too low! Guess Again: "))
        elif guess > num:
            guess = int(input("Too high! Guess Again: "))
        elif guess == num:
            response = input("That's it! Would you like to play again? (yes/no) ").lower()
            if response == "no":
                print("Thanks for playing")
                return False
            elif response == "yes":
                return True

value = True

while value:
    num = generate_number()
    guess = take_number()
    value = check_number(guess, num)
