from random import randint

t = ["Rock, Paper, Scissors"]
computer = t[randint(0,2)]
player = False

while player == False:
    print ("Lets play rock paper scissors")
    player = input["Rock", "Paper", "Scissors"]
    if player == computer:
        print ("Tie")
    elif player == ("Rock"):
        if computer == ("Paper"):
            print ("You lost, computer picked paper!")
        elif computer == ("Scissors"):
            print("You won, computer picked Scissors")
    elif player == ("Paper"):
        if computer == ("Scissors"):
            print("You lost, computer picked scissors")
        elif computer == ("Rock"):
            print("You won! Computer picked Rock!")
    elif player == ("Scissors"):
        if computer == ("Rock"):
            print ("You lost! Computer picked rock!")
        elif computer == ("Paper"):
            print ("You won, computer picked paper!")
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
player = False
computer = t[randint(0,2)]