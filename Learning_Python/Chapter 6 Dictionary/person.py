""" Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You 
should have keys such as first_name, last_name, age, and city. Print each 
piece of information stored in your dictionary"""

person = { 
    'First Name': "Favour",
    'Last Name': "Peter",
    "age": 19,
    'city': "Port Harcourt"
}
print(f"My name is {person['First Name']} {person['Last Name']} and my age is {person['age']}, "
      f"I am from {person['city']}")
