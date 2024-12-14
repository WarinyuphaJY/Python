import pgzrun
from random import randint

def draw():
    if Game_Over:
        screen.fill('pink')
        screen.draw.text(f'Time out!, your score : {Score}', (200, 300), fontsize=50)
    else:
        screen.fill( (100, 200, 100) )
        screen.draw.text(f'Score : {Score}', (5, 10), fontsize=30)
        screen.draw.text(f'Time : {Time}', (690, 10), fontsize=30)
        fox.draw()
        coin1.draw()
        coin2.draw()
        coin3.draw()

def on_key_down(key, mod, unicode):
    global Score, Time, Game_Over
    if Game_Over:
        if key == keys.RETURN:
            Score = 0
            Time = 0
            Game_Over = False
            place_coin()
            fox.pos = (WIDTH/2,HEIGHT/2)
            clock.schedule_interval(count_time, 1.0)

def place_coin1():
    coin1.x = randint(coin1.width, WIDTH - coin1.width)
    coin1.y = randint(coin1.height, HEIGHT - coin1.height)

def place_coin2():
    coin2.x = randint(coin2.width, WIDTH - coin2.width)
    coin2.y = randint(coin2.height, HEIGHT - coin2.height)

def place_coin3():
    coin3.x = randint(coin3.width, WIDTH - coin3.width)
    coin3.y = randint(coin3.height, HEIGHT - coin3.height)
    
def update():
    global Score
    if (keyboard.LEFT):
        fox.x -= 6
    elif (keyboard.RIGHT):
        fox.x += 6
    if (keyboard.UP):
        fox.y -= 6
    elif (keyboard.DOWN):
        fox.y += 6

    if (fox.colliderect(coin1)):
        sounds.ping.play()
        Score += 1
        place_coin1()

    if (fox.colliderect(coin2)):
        sounds.ping.play()
        Score += 1
        place_coin2()

    if (fox.colliderect(coin3)):
        sounds.ping.play()
        Score += 1
        place_coin3()

    if fox.x > 800:
        fox.x = 800
    if fox.y > 600:
        fox.y = 600
    if fox.x < 0:
        fox.x = 0
    if fox.y < 0:
        fox.y = 0

def count_time():
    global Time, Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

TITLE = 'Pygame Zero Game' 
WIDTH, HEIGHT = 800, 600
Score  = 0
Time = 0
Game_Over = False
MAX_TIME = 40
fox = Actor('fox', (WIDTH/2,HEIGHT/2))
coin1 = Actor('coin')
coin2 = Actor('coin')
coin3 = Actor('coin')
place_coin1()
place_coin2()
place_coin3()
clock.schedule_interval(count_time, 1.0)
pgzrun.go()
