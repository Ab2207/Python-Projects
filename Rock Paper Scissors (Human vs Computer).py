from random import randint

choice = ["rock", "paper", "scissors"]
computer = choice[randint(0,2)]
human = False

def rps(computer, human):
    while human == False:
        human = input("Rock, Paper, Scissors, Shoot! ").lower()

        if computer == "rock":               #Use case Rock
            if human == "scissors":
                print("{} beats {}.. Computer Wins!!".format(computer, human))
            elif human == "paper":
                print("{} beats {}.. Human Wins!!".format(human, computer))
            else:
                print("Tie.. Shoot again!!")

        elif computer == "paper":            #Use Case Paper
            if human == "scissors":
                print("{} beats {}.. Human Wins!!".format(human, computer))
            elif human == "rock":
                print("{} beats {}.. Computer Wins!!".format(computer, human))
            else:
                print("Tie.. Shoot again!!")

        elif computer == "scissors":         #Use Case Scissors
            if human == "rock":
                print("{} beats {}.. Human Wins!!".format(human, computer))
            elif human == "paper":
                print("{} beats {}.. Computer Wins!!".format(computer, human))
            else:
                print("Tie.. Shoot again!!")

        else:
            print("Invalid choice.. Try again..")

    return "Game Over"

print(rps(computer, human))
