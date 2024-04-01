""" Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by
adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified."""


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians_list = []
    for magician in magicians:
        great_magicians_list.append('Great ' + magician)
    return great_magicians_list


list_of_magicians = ['Oliver', 'Artur', 'Merlin', 'Hex', 'Sabrina']
show_magicians(make_great(list_of_magicians))
show_magicians(list_of_magicians)
