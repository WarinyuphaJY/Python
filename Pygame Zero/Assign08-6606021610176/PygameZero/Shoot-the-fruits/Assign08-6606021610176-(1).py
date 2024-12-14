import pgzrun
from random import randint

def draw():
    if Game_Over:
        screen.fill('purple')
        screen.draw.text(f'Time out! Your Score : {Score}', (200, 300), fontsize=50)
    else:
        screen.fill( (100, 200, 200) )
        screen.draw.text(f'Time : {Time}', (10, 10), fontsize=30)
        screen.draw.text(f'Score : {Score}', (690, 10), fontsize=30)
        apple.draw()
        orange.draw()
        pineapple.draw()

def place_apple():
    apple.x = randint(apple.width, WIDTH - apple.width)
    apple.y = 0
    apple.speed = randint(3, 7)

def place_orange():
    orange.x = randint(orange.width, WIDTH - orange.width)
    orange.y = 0
    orange.speed = randint(3, 7)

def place_pineapple():
    pineapple.x = randint(pineapple.width, WIDTH - pineapple.width)
    pineapple.y = 0
    pineapple.speed = randint(3, 7)

def count_time():
    global Time, Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = True
        clock.unschedule(count_time)

def on_mouse_down(pos, button):
    global Score
    if button == mouse.LEFT and apple.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_apple()
    elif button == mouse.LEFT and orange.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_orange()
    elif button == mouse.LEFT and pineapple.collidepoint(pos):
        sounds.ping.play()
        Score += 1
        place_pineapple()

def update():
    apple.y += apple.speed
    if (apple.y > HEIGHT):
        place_apple()
        
    orange.y += orange.speed
    if (orange.y > HEIGHT):
        place_orange()
        
    pineapple.y += pineapple.speed
    if (pineapple.y > HEIGHT):
        place_pineapple()

WIDTH = 800
HEIGHT = 600
TITLE = 'Shoot the fruits'
Score = 0
Time = 0
Game_Over = False
MAX_TIME = 40
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')
place_apple()
place_orange()
place_pineapple()
clock.schedule_interval(count_time, 1.0)
pgzrun.go()
