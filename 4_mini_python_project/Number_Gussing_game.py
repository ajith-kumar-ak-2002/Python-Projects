#Number Guessing Game

import random

secret_number = random.randint(1, 100)

attempts = 5 
while attempts > 0:
    guess = int(input("Guess a number betwwen 1 and 100:"))

    if guess == secret_number:
        print("Congrates you guessed the correct Number! ")
        break
    elif guess < secret_number:
        print("your guess is too Low, try again! ")

    else:
        print("your guess is too high, try again! ")


    attempts -=1
    print(f"you have {attempts} attempts left.")

if attempts == 0:
    print(f"Sorry, You have used all your attempts. The Secret Number was: {secret_number}")