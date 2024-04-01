""" Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges."""


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
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("The Admin privileges are: ")
        for privilege in self.privileges:
            print(privilege)


# admin = Admin("Administrator", "", role="IT Manager", salary="$40000")
# admin.privileges.show_privileges()
