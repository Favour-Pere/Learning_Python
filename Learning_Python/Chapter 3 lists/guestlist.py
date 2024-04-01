# Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting 
# them to dinner

list = ["Favour", "Mum", "Dad", "Sopreye"]

print("I am inviting you to dinner " + list[0])
print("I am inviting you to dinner " + list[1])
print("I am inviting you to dinner " + list[2])
print("I am inviting you to dinner " + list[3])

# Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the 
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still 
# in your list.

print("Sopreye won't be able to make it")

list[3] = "Benedict"

print("I am inviting you to dinner " + list[0])
print("I am inviting you to dinner " + list[1])
print("I am inviting you to dinner " + list[2])
print("I am inviting you to dinner " + list[3])

#  More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a 
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

print("I found a bigger dinner table ")

list.insert(0, "Fortune")
list.insert(3, "Rejoice")
list.insert(6, "Ina")

print("I am inviting you to dinner " + list[0])
print("I am inviting you to dinner " + list[1])
print("I am inviting you to dinner " + list[2])
print("I am inviting you to dinner " + list[3])
print("I am inviting you to dinner " + list[4])
print("I am inviting you to dinner " + list[5])
print("I am inviting you to dinner " + list[6])


#  Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.

print()

print("I am sorry, I can only invite two people for dinner.")
print("I am sorry, " + list.pop() + " I can't make it to dinner.")
print("I am sorry, " + list.pop() + " I can't make it to dinner.")
print("I am sorry, " + list.pop() + " I can't make it to dinner.")
print("I am sorry, " + list.pop() + " I can't make it to dinner.")
print("I am sorry, " + list.pop() + " I can't make it to dinner.")

del list[0]
del list[0]


print(list)

"""
Dinner Guests: Working with one of the programs from Exercises 3-4 
through 3-7 (page 46), use len() to print a message indicating the number 
of people you are inviting to dinner
"""

print("The amout of guest i am inviting is " + str( len(list)))
