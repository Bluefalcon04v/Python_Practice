""" Play rock-paper-scissor with computer"""

import random
print('let\'s play Rock, Paper, Scissor.')

def play():

    user = input("what is your choice? \n"
                     "p for paper, s for scissor, r for rock\n").lower()
    bot = random.choice(['p', 's', 'r'])                                    # computer will choose one of the following.

    while user != 's' and user != 'p' and user != 'r':
            user = input("invalid input. Try again.").lower()

    else:
        if user == bot:
             return "it's an tie"

        if win (user, bot):
            return 'you won!'

        return 'you lost.'


#r > s, s > p, p > r
def win(user,bot):

    if (user == 'r' and bot == 's') or (user == 's' and bot == 'p') or (user == 'p' and bot == 'r'):
        return True

i = 1
while i <= 5:
    print(play())
    i +=1
