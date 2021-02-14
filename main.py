import agent
import game
import numpy as np
import os

my_game = game.Game(4)

state = False

while not my_game.gameOver():
    my_game.render()
    try:
        action = int(input())
    except:
        pass
    my_game.step(action)
    os.system('clear')
print("Игра окончена!")

