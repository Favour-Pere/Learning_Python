"""User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop"""


def make_album(singer, album_title, tracks=''):
    if tracks:
        album = {'Artist': singer, 'Title': album_title, 'Number of tracks': tracks}
    else:
        album = {'Artist': singer, 'Title': album_title}

    return album


while True:
    print('\nPlease Enter your an  artist and album')
    print('Enter q to quit')

    artist = input("Enter an artist")
    if artist == 'q':
        break

    title = input('Enter a Title: ')
    if title == 'q':
        break

    artist_album = make_album(artist, title)
    print('The artist is ' + artist_album['Artist'] + ' and the album is ' + artist_album['Title'])