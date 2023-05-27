from settings import *

def diff():
    global difficulty
    state_file = open('State.txt', 'r')
    state = int(state_file.read())
    if state > 0 and state % 5 == 0:
        difficulty += 0.001
    elif state < 5:
        difficulty = 1
    elif difficulty > 8:
        difficulty = 8
    return difficulty