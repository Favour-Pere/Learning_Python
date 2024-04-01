"""7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
 Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made."""

sandwich_orders = ["bread and butter", 'beef', 'chicken', 'meat', "tuna"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich_order = sandwich_orders.pop()
    print("I made your " + current_sandwich_order.lower() + " sandwich")
    finished_sandwiches.append(current_sandwich_order)

print("\nSandwiches made")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# for sandwich_order in sandwich_orders:
#     print(f"I made your {sandwich_order}")
#     finished_sandwiches.append(sandwich_order)
#
# print()
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)
