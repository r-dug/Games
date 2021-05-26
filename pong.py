'''credit: TokyoEdtech'''

import turtle
from playsound import playsound



win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# points
score_a = 0
score_b = 0

# scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font=("Courier", 24, 'normal'))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(370, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(-370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('blue')
ball.shapesize(stretch_wid=.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = -.1


# movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)

# exit command
def exit_command():
    exit()

# keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    win.update()

    # move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font=("Courier", 24, 'normal'))


    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font=("Courier", 24, 'normal'))


    if ball.xcor() = 360 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50:
        ball.setx(360)
        ball.dx *= -1
        playsound("mario_grunt.wav")

    if ball.xcor() = -360 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50:
        ball.setx(-360)
        playsound("mario_grunt.wav")
        ball.dx *= -1
