# Write your code here :-)
import random

def draw_welcome_sign():
    print("=================== welcome to rock paper sissers========================================")

def get_user_rps():
    #get a user imputy rock paper sissor
    rps = input ('<R>ock, <P>aper, <s>issor, or e<X>it')
    return rps
    print(f"\nYou chose {rps}, computer chose {compaction}.\n")
    print(compaction,rps)
def validate_input():
    pass

def get_computer_rps():
    actions= ['rock, paper, scissors']
    compaction= random.choice(actions)

def who_won():
    pass



draw_welcome_sign()
for play in range(3):
    get_user_rps()
    get_computer_rps()
