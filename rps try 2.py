# Write your code here :-)
import random
while True:

    rps=input('enter a choice (rock, paper, scissors):')

    actions = ['rock', 'paper', 'scissors',]
    computerchoice = random.choice(actions)
    print(f"\nYou chose {rps}, computer chose {computerchoice}.\n")

    if rps == computerchoice:
        print(f"both players selected {rps}. its a tie.")
    elif rps =='rock':
        if computerchoice == 'scissors':
            print('you win. rock breaks scissors.')
        else:
            print('paper covers rock. you lose')
    elif rps == "paper":
        if computerchoice == 'rock':
            print('paper covers rock. you win')
        else:
            print('scissors cut paper. you lose')

    elif rps == 'scissors':
        if computerchoice == 'paper':
            print('scissors cut paper. you win')
        else:
            print('rock smashes scissors. you lose.')


    playagain = input('wanna go again? (y/n):')
    if playagain.lower() !='y':
        break
