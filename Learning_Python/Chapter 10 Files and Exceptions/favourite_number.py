"""Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file.
Write a separate program that reads in this value and prints the message, “I know your favorite
number! It’s _____.”"""

import json

try:
    number = int(input('Enter your favourite number '))
    file_name = "favourite_number.json"

    with open(file_name, 'w') as file_object:
        json.dump(number, file_object)

    with open(file_name, 'r') as file_object:
        number = json.load(file_object)
        print(f"I know your favourite number! It's {number}")

except ValueError:
    print('Not a number')
