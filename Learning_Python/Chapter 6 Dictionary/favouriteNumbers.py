""" Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program"""

favourite_numbers = {
    'Pere' : 7,
    'Powei' : 6,
    'Favour' : 2,
    'Rejoice': 20,
    'Fortune': 4
}

for name, number in sorted(favourite_numbers.items()):
    print(f"{name} {number}")