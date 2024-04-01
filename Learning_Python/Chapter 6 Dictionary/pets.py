""" Pets: Make several dictionaries, where the name of each dictionary is the 
name of a pet. In each dictionary, include the kind of animal and the owner’s 
name. Store these dictionaries in a list called pets. Next, loop through your list 
and as you do print everything you know about each pet"""

pets = [
    {
    "name": "dog", 
    "kind": "mammal", 
     "owner": "John"
    },

    {
    "name": "cat",
    "kind": "mammal",
    "owner": "Jane"
    },

    {
    "name": "bird",
    "kind": "bird",
    "owner": "Jim"
    }
]

for pet in pets:
    print(f"Name: {pet['name']}, Kind: {pet['kind']}, Owner: {pet['owner']}")
