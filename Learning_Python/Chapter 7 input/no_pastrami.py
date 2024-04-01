""" No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches."""

sandwich_orders = ['pastrami', "bread and butter", 'egg', 'pastrami', 'beef', 'chicken', 'meat', "tuna", "pastrami"]
finished_sandwiches = []

print("The deli has ran out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich_order = sandwich_orders.pop()
    print("I made your " + current_sandwich_order.lower() + " sandwich")
    finished_sandwiches.append(current_sandwich_order)

print("\nSandwiches made")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

