import random

# unfinished prisoners_dilemma code

def mySolution(history):
    if len(history) == 0:
        return "betray"
    if len(history) > 0:
        check = []
        (you, them) = history[-1] #Access the most recent move made by both players. History is always a list of tuples consisting of your move and then your opponent's move.
        check.append(them)
        if "c" in check:
            number = random.randint(1,10)
            if number == 10:
                return "betray"
    else:
        return "collude"
    return "betray"

history = [(" ", input("Action: "))]
while(True):
    move = mySolution(history)
    print(move)
    history.append((move, input("Action: ")))