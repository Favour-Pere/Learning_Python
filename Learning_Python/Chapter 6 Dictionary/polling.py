""" Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take 
the pol"""

favorite_languages = {
'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 'pere': 'Java'
 }

polltakers = ['pere', 'fortune', 'sopreye', 'marvellous', 'sarah']

for polltaker in polltakers:
    if polltaker in favorite_languages.keys():
        print(f"{polltaker.title()} Thank you for responding to the poll")
    else:
        print(f"{polltaker.title()} Please take the pol")
