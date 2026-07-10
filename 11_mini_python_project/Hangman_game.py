import random

words = ["python", "java", "computer", "programming", "handman", "keyboard"]

words = random.choice(words)
guessed_letters = []
attempts = 5

while attempts > 0:
    display_words = ""

    for letter in words:
        if letter in guessed_letters:
            display_words += letter + " "
        else:
            display_words += "_ "

    print("\nWord: ", display_words)

    if "_" not in display_words:
        print("Congratulations! You Guessed the word: ", words)
        break

    guess = input("Guess a Letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please Enter a Single Alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You are already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in words:
        print("Good Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left: ", attempts)

    if attempts == 0:
        print("\nGame Over!")
        print("The Word Was: ", words)
