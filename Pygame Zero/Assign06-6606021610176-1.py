import pgzrun
import random

def draw():
    screen.fill(BGColor)
    screen.draw.text("Show Rectangle",(250,10),fontsize =28,color='blue')
    for OOO in range(len(OOOOOOOO)): screen.draw.text(OOOOOOOO[OOO][2],(120*OOO,OOOOOOOO[OOO][0]),fontsize = 30,color='red')

def update():
    global OOOOOOOO
    for OOO in range(len(OOOOOOOO)): OOOOOOOO[OOO][0] = 0 if OOOOOOOO[OOO][0] > HEIGHT else OOOOOOOO[OOO][0] + OOOOOOOO[OOO][1]

TITLE = "TEXT"
WIDTH = 640
HEIGHT = 480
OOOOOOOO = [[HEIGHT/2,random.randint(1,4),input("Enter Text "+str(x+1)+" : ")] for x in range(5)]
BGColor = (255,255,255)
pgzrun.go()
