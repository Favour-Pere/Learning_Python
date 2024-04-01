""" Restaurant Seating: Write a program that asks the user how many people 
are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready."""

people = int(input("How many people are in the dinner group? "))

if people > 8:
    print("You would have to wait for a table")
else:
    print("The table is ready")

