""" Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number."""

while True:
    print('Give me two numbers and i will add it ')

    try:
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        num3 = num1 + num2
        print(num3)
        break
    except TypeError:
        print("Only input a number")
        continue
    except ValueError:
        print("Only Enter a number")
        continue
