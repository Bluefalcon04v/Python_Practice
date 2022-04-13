"""it is a speed typing game in which countdown is running in the background, and we have to type 20 words in given time"""

import random
import string
from time import *
import threading     # it will help us to run 2 or more program at the same time


def countdown():
    global my_timer         # defining it as a global, so we can use it in while loop later
    my_timer = 12           # +2 second is to read menu
    for x in range(12):
        my_timer -= 1
        sleep(1)
    print("\nout of time")

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()

print("""Welcome to speed typing game.
You have to type 20 words in 10 seconds with best accuracy as you can""")
score = 0
i = 1
global my_timer
 
while my_timer > 0:
    while i <= 20 and my_timer != 0:
        random_letter = random.choice(string.ascii_letters)
        print(f"{i}) {random_letter}")
        inp = input()
        if random_letter == inp:
            print("correct input")
            score +=1
        else:
            print("wrong input")
        i += 1

print(f"Your score is: {score} \nYour accuracy is: {score/20*100}%, Thankyou!")