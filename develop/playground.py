import random
import socket
import operator
from basic import basic_variables

print("These are your options: \n")
print("Option 1: Basic Variables in String \n")
print("Option 2: Number Guessing \n")
print("Option 3: Get your local IP \n")
print("Option 4: Calculate \n")
print("Option 5: Roll a Dice \n")

# print(" \n")

while True:

    choice = input("Make a choice and pick a number: \n")

    if choice == "1":


        """
        name = input("Tell me your name: \n")
        age = input("Tell me your age: \n")
        place = input("Tell me where you live: \n")

        print("Your name is " + name + ", you are " + age + " years old and live in " + place + "\n")
        exit()
        """

        basic_variables()

    elif choice == "2":
        r = int(random.randint(0, 100))
        a = -1
        # print("Your guess is " + a + " and the random number is % d" % (r) + "\n")
        print(r)

        while r != a:
            a = int(input("Enter your guess: \n"))
            if r == a:
                print("You did it, the correct number is %d" % a)
                exit()
            elif r >= a:
                print("Your number is too small")
            elif r <= a:
                print("Your number is too big")

    elif choice == "3":
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print(local_ip)
        exit()

    elif choice == "4":

        while True:
            print("What would you like to do?: \n")
            print("+ - Add \n")
            print("- - Subtract \n")
            print("* - Multiply \n")
            print("/ - Divide \n")

            o = input("Pick an operator: \n")

            ops = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
            }

            a = int(input("Enter a number: \n"))
            b = int(input("Enter a second number: \n"))

            print(ops[o](a, b))
            exit()

    elif choice == "5":

        while True:
            try:
                dice_amount = int(input("How many Dices do you want to roll?: \n"))

                i = 1

                while i <= dice_amount:
                    dice_output = int(random.randint(1, 6))

                    print(f"Dice {i}: {dice_output}")

                    i += 1

                exit()

            except ValueError:
                print("Error, try again!")

    else:
        print("Invalid Input, retry")
