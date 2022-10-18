import time
from playsound import playsound


def countdown(t):
    while t:
        min, sec = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(t)

    print('Fire in the hole!!')
    playsound("/Users/marvinquirmbach/Documents/YouTube Downloads/Nuke Sound Effect.mp4")


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))