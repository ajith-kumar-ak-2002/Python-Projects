import random
import string

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)
    print(f"Your Generated Password is: {password}")