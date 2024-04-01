""" Glossary 2: Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your 
glossary. When you run your program again, these new words and meanings 
should automatically be included in the output"""

glossary = {
    'varible' : 'A storage location in memory that stores data',
    'list' : 'a collection of data',
    'array': 'a matrix of data',
    'for' : 'a type of loop for __ in __ '
}
glossary['dictionary'] = 'Key pair Values'

for name, defination in sorted(glossary.items()):
    print(f"{name}: {defination}")