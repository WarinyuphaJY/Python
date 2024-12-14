import pgzrun

def draw():
    screen.fill('white')
    if Index == 1:
        emotionaldamage.draw()
    elif Index == 2:
        goku.draw() 
    elif Index == 3:
        cloud.draw()
    elif Index == 4:
        lionking.draw()
    elif Index == 5:
        initiald.draw()

def on_key_down(key, mod ,unicode):
    global Index
    if (key == keys.K_1):
        music.play('emotional-damage')
        Index = 1
    elif (key == keys.K_2):
        music.play('drip-goku-meme')
        Index = 2
    elif (key == keys.K_3):
        music.play('victory-ff7')
        Index = 3
    elif (key == keys.K_4):
        music.play('the-lion-sleeps-tonight')
        Index = 4
    elif (key == keys.K_5):
        music.play('initial-d')
        Index = 5
    elif (key == keys.S):
        music.stop()

def update():
    global Index
    if Index == 1:
        emotionaldamage.x += 1
        if emotionaldamage.x == 1024:
            emotionaldamage.x = 0
    elif Index == 2:
        goku.x += 1
        if goku.x == 1024:
            goku.x = 0
    elif Index == 3:
        cloud.x += 1
        if cloud.x == 1024:
            cloud.x = 0
    elif Index == 4:
        lionking.x += 1
        if lionking.x == 1024:
            lionking.x = 0
    elif Index == 5:
        initiald.x += 1
        if initiald.x == 1024:
            initiald.x = 0

TITLE = 'Slide Show Images & Play Music or Sounds'
WIDTH = 1024
HEIGHT = 768
Index = 0
emotionaldamage = Actor('emotionaldamage')
goku = Actor('goku')
cloud = Actor('cloud')
lionking = Actor('lionking')
initiald = Actor('initiald')
pgzrun.go()
