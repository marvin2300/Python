import random

r = int(random.randint(0, 100))
a = -1
guesses = 1

# print("Your guess is " + a + " and the random number is % d" % (r) + "\n")
print(r)

while r != a:
    a = int(input("Enter your guess: \n"))
    if r == a:
        print(f"You did it, the correct number is {a}!")
        if guesses == 1:
            print(f"You needed {guesses} guess!")
        else:
            print(f"You needed {guesses} guesses!")
            exit()
    elif r >= a:
        print("Your number is too small")
        guesses += 1
    elif r <= a:
        print("Your number is too big")
        guesses += 1