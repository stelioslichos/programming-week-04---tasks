# The Number Guessing Game
import random
# randomly generate a number between 1 and 10
secret_guess = random.randint(1,10)
# to pass the test uncomment this line
secret_guess = 4

print("Welcome to the Number Guessing Game!")
print("You need to try and guess the number between 1 and 10...")
print("If you wish to exit the game enter 0..")

guess = int(input("Please enter a guess:\n"))

while guess != secret_guess and guess != 0:
    print("That is not correct, please try again.")
    guess = int(input("Please enter a guess:\n"))

if guess != 0:
    print(f"Well done the correct answer is {secret_guess}")