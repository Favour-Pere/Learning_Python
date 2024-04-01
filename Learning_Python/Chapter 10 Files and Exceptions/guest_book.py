"""Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file."""

while True:
    guest_name = input("Please enter your name? ")
    if guest_name == 'q':
        break
    else:
        print(f'Greetings {guest_name}')
        with open('guest_book.txt', 'a') as file:
            file.write(f"{guest_name} \n")