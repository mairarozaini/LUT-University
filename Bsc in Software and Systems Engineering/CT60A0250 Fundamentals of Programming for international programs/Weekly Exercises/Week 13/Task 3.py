import random

random.seed(42)
CHOICES = ["Rock", "Paper", "Scissors"]

while True:
    user = input("Rock, Paper, Scissors (type 'Exit' to quit):\n")
    computer = CHOICES[random.randint(0,2)]
    if user == "Exit":
        break
    elif user == computer:
        print("It was a tie!")
    elif user == "Rock" and computer == "Paper":
        print("You lost! Rock loses to Paper")
    elif user == "Rock" and computer == "Scissors":
        print("You won! Rock triumphs Scissors")
    elif user == "Paper" and computer == "Rock":
        print("You won! Paper triumphs Rock")
    elif user == "Paper" and computer == "Scissors":
        print("You lost! Paper loses to Scissors")
    elif user == "Scissors" and computer == "Paper":
        print("You won! Scissors triumphs Paper")
    elif user == "Scissors" and computer == "Rock":
        print("You lost! Scissors loses to Rock")
    else:
        print("That's not a valid play. Check your spelling!")




