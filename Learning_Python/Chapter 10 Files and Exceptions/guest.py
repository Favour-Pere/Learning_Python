"""Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt"""

guest_name = input("Please enter your name? ")

with open('guest.txt', 'a') as file:
    file.write(f"{guest_name} was invited\n")
