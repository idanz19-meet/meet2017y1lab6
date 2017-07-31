UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

import turtle

direction = UP

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = "space"

def up():
    global direction
    direction = UP
    print("YOU FREAKING PRESSED UP, DUDE!!!")
    turtle.pos()
    

def left():
    global direction
    direction = LEFT
    print("YOU FREAKING PRESSED LEFT, DUDE!!!")

def down():
    global direction
    direction = DOWN
    print("YOU FREAKING PRESSED DOWN, DUDE!!!")

def right():
    global direction
    direction = RIGHT
    print("YOU FREAKING PRESSED RIGHT, DUDE!!!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()



