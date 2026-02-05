import turtle 
import math
import random

# Variables
speed = 3
score = 0
chances = 3
gameover = False
#  Arrays
bg_colors = ["lightyellow","lightblue","lightgreen","lavender","honeydew",
    "mistyrose","aliceblue","lightcyan","peachpuff","whitesmoke"]


food_colors = [ "darkred","darkblue","darkgreen","darkmagenta", "darkcyan",
    "maroon","navy","purple","brown","darkorange"]


food_shape = ["circle","square","triangle","arrow","classic"]
#Screen setup  
screen = turtle.Screen()
screen.setup(1.0,1.0)
screen.title("Turtle Game")

# Welcome msg
top_msg = turtle.Turtle()
top_msg.penup()
top_msg.hideturtle()
top_msg.speed(0)
top_msg.goto(0,310)
top_msg.write("WELCOME TO MY GAME",align="center",font=("",25,""))

# Player Setup
player = turtle.Turtle()
player.shape("turtle")
player.color("magenta")
player.shapesize(2)
player.penup()
player.speed(0)
player.goto(0,0)

# Food Setup
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(1)
food.penup()
food.speed(0)
food.goto(400,200)

# Score
score_msg = turtle.Turtle()
score_msg.hideturtle()
score_msg.penup()
score_msg.speed(0)
score_msg.goto(-500,310)
score_msg.write(f"Score = {score}",align="center",font=("",25,""))

# Chances
chances_msg = turtle.Turtle()
chances_msg.hideturtle()
chances_msg.penup()
chances_msg.speed(0)
chances_msg.goto(500,310)
chances_msg.write(f"Chances = {chances}",align="center",font=("",25,""))

# Game Over
msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.speed(0)

# Duplicate Food 
food_d = turtle.Turtle()
food_d.penup()
food_d.speed(0)
food_d.hideturtle()

# Functions Responsible for Directional Movement 
def right():
    player.setheading(0)

def left():
    player.setheading(-180)

def Up():
    player.setheading(90)

def Down():
    player.setheading(-90)

def restart():
    global gameover,score , chances , speed 
    msg.clear()
    msg.goto(4000,5000)
    score = 0
    score_msg.clear()
    score_msg.write(f"Score = {score}",align="center",font=("",25,""))

    chances = 3
    chances_msg.clear()
    chances_msg.write(f"Chances = {chances}",align="center",font=("",25,""))

    player.showturtle()
    food.showturtle()
    speed = 3

# Keys Setup which calls the fuction for the movement 
screen.listen()
screen.onkey(right,"Right")
screen.onkey(left,"Left")
screen.onkey(Up,"Up")
screen.onkey(Down,"Down")
screen.onkey(restart,"space")


# While loop for automation 
while not gameover:

    rs = random.choice(food_shape)   # Generate random Shape
    rc = random.choice(food_colors)  # Generate random Color
    rb = random.choice(bg_colors)    # Generate random Bg Color


    player_x = player.xcor()
    player_y = player.ycor()

    food_x = food.xcor()
    food_y = food.ycor()

    food_dx = food_d.xcor()
    food_dy = food_d.ycor()


    #  Scene for game over 
    if chances == 0:
        msg.write("GAME OVER",align="center",font=("",25,""))
        msg.goto(0,0)
        player.hideturtle()
        food.hideturtle()

    # To eat food condition  
    distance = math.dist((player_x,player_y),(food_x,food_y)) 
    if distance<20:
        
        food_x = random.randint(-400,400)
        food_y = random.randint(-200,200)
        food.goto(food_x,food_y)
        food.shape(rs)
        food.color(rc)
        
        score = score+1  #increment score 
        score_msg.clear()
        score_msg.write(f"Score = {score}",align="center",font=("",25,""))

        if score % 3 == 0 and score > 0: #Changing Background Color
            screen.bgcolor(rb)
            speed = speed+2
        
        if score == 3:

            food_dx = food_d.xcor()
            food_dy = food_d.ycor()

            dx = random.randint(-200,200)
            dy = random.randint(-200,200)
            ds = random.choice(food_shape)
           
            food_d.goto(dx,dy)
            food_d.shape(ds)

            food_d.showturtle()

        if score >= 7:
            food_d.hideturtle()

    # Decrement of Chance 
    if player_x <-590 or player_x>590 or player_y <-280 or player_y>280:
        chances = chances - 1
        chances_msg.clear()
        chances_msg.write(f"Chances = {chances}",align="center",font=("",25,""))
        player.goto(0,0)

        
    player.forward(speed)
    screen.update()


