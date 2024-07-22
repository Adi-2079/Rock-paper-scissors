from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]
player = False

while player == False:
    print("Let's play Rock, Paper, Scissors")
    player = input("Rock", "Paper", "Scissors ")
    
    if player == computer:
        print("It's a tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost! Computer picked Paper.")
        elif computer == "Scissors":
            print("You won! Computer picked Scissors.")
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost! Computer picked Scissors.")
        elif computer == "Rock":
            print("You won! Computer picked Rock.")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost! Computer picked Rock.")
        elif computer == "Paper":
            print("You won! Computer picked Paper.")
    else:
        print("That's not a valid play. Check your spelling!")

    # Reset player to False so the loop can continue
    player = False
    computer = t[randint(0, 2)]