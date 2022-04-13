import random
import string

print("""Welcome to Typing Test
to END the game type end\n""")
score = 0
i = 1
while i <= 26:
    random_letter = random.choice(string.ascii_letters)
    print(f"{i}) {random_letter}")
    inp = input()
    if random_letter == inp:
        print("correct input")
        score +=1
    elif inp == "end" or "END":
        print("You have ended the Typing test ")
        break
    else:
        print("wrong input")

    i += 1

print(f"Your accuracy is: {score/26*100}%, Thankyou!")