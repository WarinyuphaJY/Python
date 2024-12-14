import pgzrun

def draw():
    screen.fill((41,131,132))

    boy.draw()

def reset_boy():
    boy.pos = (boy.WIDTH/2,boy,HEIGHT/2)

def count_index():
    global index,walk
    if walk == "Down":
       index += 1
       if index == 4:
          index = 0
       boy.image = images_boy[index]

    elif walk == "Up":
       index += 1
       if index == 4:
          index = 0
       boy.image = images_boy_back[index]

    elif walk == "Left":
       index += 1
       if index == 4:
          index = 0
       boy.image = images_boy_left[index]

    elif walk == "Right":
       index += 1
       if index == 4:
          index = 0
       boy.image = images_boy_right[index]
    else:
       walk = "Not"
       index = 0

def update():
   global walk,index
   if(keyboard.LEFT):
      boy.x -= 2
      walk = "Left"
   elif (keyboard.RIGHT):
      boy.x += 2
      walk = "Right"
   elif (keyboard.UP):
      boy.y -= 2
      walk = "Up"
   elif (keyboard.DOWN):
      boy.y += 2
      walk = "Down"
   else:
      index = 0
      walk = "Not" 
   if boy.x >= WIDTH:
      
      boy.x = 0
   elif boy.x < 0:
      boy.x = WIDTH - 1
   if boy.y >= HEIGHT:
      boy.y = 0
   elif boy.y < 0:
      boy.y = HEIGHT - 1

#Main Program
TITLE = "Character Animation"
WIDTH = 800
HEIGHT = 600
index = 0
walk = "Not"

#ARRAY
images_boy = ['boy_1','boy_2','boy_3','boy_4']

boy  = Actor('boy_1',(WIDTH/2,HEIGHT/2))

images_boy_left = ['boy_5','boy_6','boy_7','boy_8']
images_boy_right = ['boy_9','boy_10','boy_11','boy_12']
images_boy_back = ['boy_13','boy_14','boy_15','boy_16']
boy1 = Actor('boy_1')
boy1 = Actor('boy_2')
boy1 = Actor('boy_3')
boy1 = Actor('boy_4')

clock.schedule_interval(count_index,0.090)

pgzrun.go()
