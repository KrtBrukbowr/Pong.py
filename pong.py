""" 
Author: Kurt Bruckbauer
Program: pong.py
Date: 4/26/20
Summary:    A pong clone powered by Python 
 """
import turtle
import winsound
 
wn = turtle.Screen()
wn.title("Pong by Kurt Bruckbauer")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .1 # Every time the ball moves, it moves 2 pixels along xcor
ball.dy = .1  # Every time the ball moves, it moves 2 pixels along ycor

# Pen to write Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 25, "normal"))


# function paddle A UP
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# function, paddle A DOWN
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# function paddle B UP
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# function, paddle B DOWN
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# function to pause game

# function


# Keyboard binding
wn.listen() # Tells the window to listen for keyboard press events
wn.onkeypress(paddle_a_up, "e") # On press of "e" button perform paddle_a_up()
wn.onkeypress(paddle_a_down, "c")
wn.onkeypress(paddle_b_up, "u")
wn.onkeypress(paddle_b_down, "n")

# Sound FX variables
frequency = 220 # frequency parameter needed in Hz
duration = 150 # .15 sec, duration parameter needed in ms
paddle_frequency = 160
paddle_duration = 200


# Main game loop
while True:
    wn.update()


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 290: # Top border
        ball.sety(290)  # If the ball is greater than top Border ->
        winsound.Beep(frequency,duration)
        ball.dy *= - 1  # -> Reverse movement of the ball(Ball bounces off top wall)
        
    if ball.ycor() < -290: # Bottom border
        ball.sety(-290) # If the ball is less than the Btm Border ->
        winsound.Beep(frequency,duration)
        ball.dy *= - 1  # -> Reverse mvmnt of the ball(Ball bounces off btm wall)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= - 1 # Reverses ball movement
        score_a += 1 # Adds 1 to the Player A score
        pen.clear() # Clears the previous score
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal")) # Writes the updated score to the Window
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= - 1 # Reverses ball movement
        score_b += 1 # Adds 1 to the Player A score
        pen.clear() # Clears the previous score 
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 25, "normal")) # Writes the updated score to the Window
        
    # Paddle and Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        winsound.Beep(paddle_frequency, paddle_duration)
        ball.dx *= - 1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        winsound.Beep(paddle_frequency, paddle_duration)
        ball.dx *= - 1