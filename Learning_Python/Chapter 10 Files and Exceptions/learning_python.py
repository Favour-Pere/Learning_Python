""" Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading in the entire file,
once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block."""

with open('summary.txt') as file:
    doc = file.read()
    print(doc)

with open('summary.txt') as file_object:
    files = file_object.readlines()

    for file in files:
        print(file.replace('python', 'C'))
