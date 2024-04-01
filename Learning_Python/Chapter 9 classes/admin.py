""" Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""


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


class Admin(User):

    def __init__(self, first_name, last_name, **attributes):
        super().__init__(first_name, last_name, **attributes)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The Admin privileges are: ")
        for privilege in self.privileges:
            print(privilege)


admin = Admin("Administrator", "", role="IT Manager", salary="$40000")

admin.show_privileges()
admin.greet_user()
admin.describe_user()
