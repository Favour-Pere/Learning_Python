"""Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list."""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


list_of_magicians = ['Oliver', 'Artur', 'Merlin', 'Hex', 'Sabrina']

show_magicians(list_of_magicians)
