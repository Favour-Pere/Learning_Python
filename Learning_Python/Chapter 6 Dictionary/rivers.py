""" Rivers: Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary."""

rivers = {
    'nile': 'egypt',
    'niger': 'nigeria',
    'lake': 'vite',
    'kola': 'add',
    'joze': 'kaima',
    'konzi': 'yola',
    'missipi': 'antantica'
}

for  river, location in rivers.items():
    print(f"The {river} runs through {location}")

print()
print("List of Rivers")
for river in rivers.keys():
    print(river)

print()
print("List of Location")
for location in rivers.values():
    print(location)