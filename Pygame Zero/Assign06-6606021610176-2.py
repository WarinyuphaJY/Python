import pgzrun

from random import randint

O = randint
def update():
    global OOOOOOOOOOOO
    for OOO in range(len(OOOOOOOOOOOO)): OOOOOOOOOOOO[OOO][0] = 0 if OOOOOOOOOOOO[OOO][0] > WIDTH else OOOOOOOOOOOO[OOO][0] + OOOOOOOOOOOO[OOO][3]


def draw():
    screen.clear()
    for OOO in range(len(OOOOOOOOOOOO)):
        screen.draw.filled_circle((OOOOOOOOOOOO[OOO][0],OOOOOOOOOOOO[OOO][1]),OOOOOOOOOOOO[OOO][2], "blue")

TITLE = 'Circle Animation'
WIDTH = 800
HEIGHT = 480
OOOOOOOOOOOO = [[O(0,WIDTH),O(0,HEIGHT),25,O(1,5)] for i in range(O(1,8))]

pgzrun.go()
