#The user of your program is playing a game of rock-paper-scissors against the computer. 
#The user is prompted to type in "rock", "paper", or "scissors". 
#The user's choice is compared to the game's choice (randomly generated). And a  winner is determined.
#The program notifies the user of the winner or the tie.
#The user is prompted to play again.
#The process repeats until the user types "stop".
#A classic game or tie breaker, the rules to rock-paper-scissors are:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
import random
import sys
def game_running():
    possible = ["Rock", "Paper", "Scissors"]
    rn = random.randint(0, 2)
    print(possible[rn])
    print()
    ai_pick = possible[rn]
    rps = input("Pick either Rock, Paper, or Scissors: ")
    if  ai_pick == "Rock":
        if rps == "scissors":
            print("You Lost")
        elif ai_pick == "rock":
            print("Tied")
        else:
            print("You won!")
    elif ai_pick == "Paper":
        if rps == "scissors":
            print("You have won")
        elif ai_pick == "paper":
            print("Tied")
        else:
            print("You lost")
    elif ai_pick == "Scissors":
        if rps == "rock":
            print("You have won")
        elif rps == "scissors":
            print("Tied")
        else:
            print("You lost")
    main()
def main():
    z = 0
    while z == 0:
        l = str(input("Enter 'y' to restart or 'stop' to end the program: "))
        if l == 'y':
            game_running()
        elif l == 'stop':
            z += 1
        else:
         print()
         print("'y' or 'stop' please.")
         sys.exit("You have exited the program.")
game_running()
            
            
            
