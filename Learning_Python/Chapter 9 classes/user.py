""" Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""


class User:

    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes

    def describe_user(self):
        profile = {'first_name': self.first_name, 'last_name': self.last_name}
        for key, value in self.attributes.items():
            profile[key] = value
        for key, value in profile.items():
            print(f'{key}: {value}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name} how are you doing? ')


user = User('Pere', 'Robert', gender='Male')

user.describe_user()
user.greet_user()
