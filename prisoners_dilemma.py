import random

# unfinished prisoners_dilemma code

def mySolution(history):
    if len(history) == 0:
        return "C"
    else:
        check = []
        (you, them) = history[-1] #Access the most recent move made by both players. History is always a list of tuples consisting of your move and then your opponent's move.
        check.append(them)
        if "C" in check:
            number = random.randint(1, 100)
            if number <= 75:
                return "B"
            else:
                return "C"
        else:
            number = random.randint(1, 100)
            if number <= 75:
                return "C"
            else:
                return "B"

history = [(" ", " ")]

while(True):
    move = mySolution(history)
    print(move)
    opponentMove = input("Action: ").upper()
    history.append((move, opponentMove))