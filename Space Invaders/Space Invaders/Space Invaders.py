# Space invaders

###
# Import needed assets.
###
import random
import turtle
import math
import os

###
# Set up the screen.
###
window = turtle.Screen()
window.bgcolor('black')
window.title('Space Invaders')
window.bgpic('starfield2.gif')

# Draw a border
border_pen = turtle.Turtle()
border_pen.speed(8)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

###
# Register shapes
###
turtle.register_shape('invader2.gif')
turtle.register_shape('player.gif')

# Set the score to 0
score = 0

###
# Draw score
###
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = 'left', font = ('Arial', 14, 'normal'))
score_pen.hideturtle()


###
# Create sprites
###

# Create the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Choose a random number of enemies.
number_of_enemies = 5
# Create an empty list of enemies.
enemies = []
# Add enemies to the list.
for i in range(number_of_enemies):
    # Create the enemy.
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color('red')
    enemy.shape('invader2.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    

# Create player bullet.
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()


###
# Set speeds.z
###
playerspeed = 15
enemyspeed = 2
bulletspeed = 20

###
# Define bullet state
# Ready - ready to fire
# Fire - bullet is firing
###
bulletstate = 'ready'


###
# Define functions
###
def move_left():
    x = player.xcor()
    x -= playerspeed
    # Boundary checking.
    if x < -280:
        x = -280
    player.setx(x)
    # Input testing.
    #print('Left key pressed.')

def move_right():
    x = player.xcor()
    x += playerspeed
    # Boundary checking.
    if x > 280:
        x = 280
    player.setx(x)
    # Input testing.
    #print('Right key pressed.')

def fire_bullet():
    # Declare bullet state as a global if it needs changed.
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        # Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def  isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() -t2.xcor(), 2 )+math.pow(t1.ycor() -t2.ycor(), 2 ))
    if distance < 15:
        return True
    else:
        return False
    
    

###
# Create keyboard bindings
###
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


###
# Main game loop
###
while True:
    
    for enemy in enemies:
        ###
        # Move the enemy
        ###
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        # Moves all enemies down.
        if enemy.xcor() >280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Changes direction.
            enemyspeed *= -1
        # Moves all enemies down. 
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Changes enemy direction.
            enemyspeed *= -1

        # Check for bullet and enemy collision
        if  isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition (0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = 'left', font = ('Arial', 14, 'normal'))


        if  isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('G A M E')
            print('O V E R')
            break
        
    # Move the bullet.
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Boundary check bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'


delay = input('Pres enter to finish...')
