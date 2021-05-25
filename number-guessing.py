import random

x = random.randrange(1, 11)

lower = ["Guess something lower, choose another: ",
         "Your number was too high, choose another: ", "Try again: "]
higher = ["Guess something greater, choose another: ",
          "Your number was too low, choose another: ", "Try again: "]

correct = False
guess = int(input("Guess the number between 1 and 10: "))
if guess == x:
    correct = True

while(correct == False):
    if(guess > x):
        guess = int(input(lower[random.randrange(0, len(lower))]))
    elif(guess < x):
        guess = int(input(higher[random.randrange(0, len(higher))]))
    else:
        correct = True

print("Congrats! That was this number!")
