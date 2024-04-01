""" Pizza Toppings: Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza."""


toppings = []

while True:
    topping = input("Enter a pizza topping to end enter quit ")
    if topping == 'quit':
        print("Thank you entering")
        print("Your toppings are: ")
        for topping in toppings:
            print(topping)
        break
    else:
        print(f"{topping} will be added to your pizza")
        toppings.append(topping)
