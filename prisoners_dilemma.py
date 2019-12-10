import random

def mySolution(history):
    (you, them) = history[-1]
    check = []
    check.append(them) # Get the action of the opponent

    # If the opponent colludes, have a 75% chance of betraying
    # and a 25% chance of colluding
    if "C" in check:
        number = random.randint(1, 100)
        if number <= 75:
            return "B"
        else:
            return "C"
    # If the opponent betrays, have a 7% chance of colluding
    # and a 25% chance of betraying
    else:
        number = random.randint(1, 100)
        if number <= 75:
            return "C"
        else:
            return "B"

# Create empty history. This will be used to store the
# history of actions.
history = [(" ", " ")]

while(True):
    move = mySolution(history)
    print(move)
    opponentMove = input("Action: ").upper() # Get the action of the opponent.
    history.append((move, opponentMove))