""" People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three 
dictionaries in a list called people. Loop through your list of people. As you 
loop through the list, print everything you know about each person."""

person1 = { 
    'First Name': "Favour",
    'Last Name': "Peter",
    "age": 19,
    'city': "Port Harcourt"
}

person2 = {
    'First Name': "Pere",
    'Last Name': "Robert",
    "age": 20,
    'city': "Bayelsa"
}

person3 = {
    'First Name': "Faith",
    'Last Name': "Peter",
    "age": 16,
    'city': "Port Harcourt"
}

people = [person1, person2, person3]

for person in people:
    print("First Name: " + person['First Name'])
    print("Last Name: " + person['Last Name'])
    print("Age: " + str(person['age']))
    print("City: " + person['city'])
    print("\n")
