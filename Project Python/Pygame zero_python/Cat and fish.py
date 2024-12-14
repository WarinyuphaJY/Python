import pgzrun
from random import randint

def draw():
    if Game_Over:
        screen.fill('pink')
        screen.draw.text(Game_Over,(320,250),fontsize=50)
        screen.draw.text('Press r to restart the game',(300,300),fontsize=50)
    else:
        if Score <= 25:
            screen.fill(('light blue'))
            screen.draw.text(f'Score : {Score}',(5,10),fontsize=30)
            screen.draw.text(f'Fish : {Fish}',(5,30),fontsize=30)
            screen.draw.text(f'Time : {Time}',(800,10),fontsize=30)
            cat.draw()
            fd1.draw()
            fd2.draw()
            fn.draw()

        elif Score <= 50:
            screen.fill((255,222,173))
            screen.draw.text(f'Score : {Score}',(5,10),fontsize=30)
            screen.draw.text(f'Fish : {Fish}',(5,30),fontsize=30)
            screen.draw.text(f'Time : {Time}',(800,10),fontsize=30)
            cat.draw()
            fd1.draw()
            fd2.draw()
            fn.draw()

        
        else:
            screen.fill((230,230,250))
            screen.draw.text(f'Score : {Score}',(5,10),fontsize=30)
            screen.draw.text(f'Fish : {Fish}',(5,30),fontsize=30)
            screen.draw.text(f'Time : {Time}',(800,10),fontsize=30)
            cat.draw()
            fd1.draw()
            fd2.draw()
            fn.draw()


def update():
    global Score,Fish,Game_Over
    if Game_Over: return;

    if (keyboard.LEFT) : cat.x -= 20
    elif (keyboard.RIGHT) : cat.x += 20
    fd1.y += fd1.speed
    if (fd1.y > HEIGHT):
        place_fd1()
    fd2.y += fd2.speed
    if (fd2.y > HEIGHT):
        place_fd2()
    fn.y += fn.speed
    if (fn.y > HEIGHT):
        place_fn()

    if cat.x > WIDTH:
        cat.x = 0
    if cat.x < 0:
        cat.x = WIDTH

    if (cat.colliderect(fd1)):
        music.play_once('cion')
        Score += 1
        place_fd1()
    if (cat.colliderect(fd2)):
        music.play_once('cion')
        Score += 1
        place_fd2()
    if (cat.colliderect(fn)):
        print("collide")
        music.play_once('meoww')
        Score -= 2
        Fish += 1
        place_fn()
        
    if Fish >= 5:
        Game_Over = f'You Die!,Your score : {Score}'
        clock.unschedule(count_time)
           

def on_key_down(key,mod,unicode):
    global Game_Over, Fish, Time, Score
    if Game_Over and key == keys.R:
        Score = 0
        Time = 0
        Fish = 0
        clock.schedule_interval(count_time,1.0)
        Game_Over = False
    



def place_fd1():
    fd1.x = randint(fd1.width, WIDTH - fd1.width)
    fd1.y = 0
    fd1.speed = randint(8,10)



def place_fd2():
    fd2.x = randint(fd2.width, WIDTH - fd2.width)
    fd2.y = 0
    fd2.speed = randint(8,10)
    
def place_fn():

    if Score <= 25:
        fn.x = randint(0, WIDTH)
        fn.y = 0
        fn.speed = 10
    elif Score <= 50:
        fn.x = randint(0, WIDTH)
        fn.y = 0
        fn.speed = 14
    else:
        fn.x = randint(0, WIDTH)
        fn.y = 0
        fn.speed = 18



    
def count_time():
    global Time,Game_Over
    Time += 1
    if Time == MAX_TIME:
        Game_Over = f'You Win!,Your score : {Score}'
        clock.unschedule(count_time)
         
#MAIN
TITLE = 'Coin Collection Gsme'
WIDTH,HEIGHT = 1000,600
cat = Actor('cat',(WIDTH/2,520))
Score = 0
Time = 0
Fish = 0
MAX_TIME = 80
Game_Over = False
fd1 = Actor('fd')
fd2 = Actor('fd')
fn = Actor('fn')
place_fd1()
place_fd2()
place_fn()
count_time()
clock.schedule_interval(count_time,1.0)

pgzrun.go()
