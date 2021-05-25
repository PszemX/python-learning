import random

possibles = ["rock", "paper", "scissors"]


def game(welcomeMsg="Let's play 'rock, paper, scissors' game. Choose one of them: "):
    botChoice = possibles[random.randrange(0, len(possibles))]
    userChoice = str(
        input(welcomeMsg)).lower()

    print(f"Your choice: { userChoice }")
    print(f"My choice: { botChoice }")
    if(botChoice == userChoice):
        print("Draw!")
        game("We can't finish yet... Pick one more time: ")
    elif((botChoice == "rock" and userChoice == "paper") or (botChoice == "paper" and userChoice == "scissors") or (botChoice == "scissors" and userChoice == "rock")):
        print("You've won!!")
    else:
        print("You've lost :<")


game()
