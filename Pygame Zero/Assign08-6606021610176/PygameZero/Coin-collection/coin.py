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
        coin.draw()


def place_coin():
    coin.x = randint(coin.width, WIDTH - coin.width)
    coin.x = randint(coin.height, HEIGHT - coin.height)
    coin.y = randint(coin.width, WIDTH - coin.width)
    coin.y = randint(coin.height, HEIGHT - coin.height)
    
def update():
    global Score
    if (keyboard.LEFT): fox.x -= 1
    elif (keyboard.RIGHT): fox.x += 1
    if (keyboard.UP): fox.y -= 1
    elif (keyboard.DOWN): fox.y += 1

    if (fox.colliderect(coin)):
        sounds.ping.play()
        Score += 1
        place_coin()

def count_time():
    global Time, Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

TITLE = 'Coin Collection Games'
WIDTH, HEIGHT = 800, 600
Score  = 0
Time = 0
Game_Over = False
MAX_TIME = 30
fox = Actor('fox', (WIDTH/2,HEIGHT/2))
coin = Actor('coin')
place_coin()
clock.schedule_interval(count_time, 1.0)
pgzrun.go()
