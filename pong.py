#%%
import turtle
import time
#%%
#create Screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

#left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid =6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

#right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid =6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

#ball
bspeed = 5
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = -1*bspeed
ball.dy = -1*bspeed

#initialize the score
left_player = 0
right_player = 0

#display the score
score = turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("0                           0",
            align = "center", font = ("Courier", 24, "normal"))

#move Paddles
def lpaddleup():
    y = left_pad.ycor()
    if y < 250:
        y+=20
        left_pad.sety(y)
def lpaddledown():
    y = left_pad.ycor()
    if y > -250:
        y-=20
        left_pad.sety(y)

def rpaddleup():
    y = right_pad.ycor()
    if y < 250:
        y+=20
        right_pad.sety(y)
def rpaddledown():
    y = right_pad.ycor()
    if y > -250:
        y-=20
        right_pad.sety(y)

sc.listen()
sc.onkeypress(lpaddleup, "w")
sc.onkeypress(lpaddledown, "s")
sc.onkeypress(rpaddleup, "Up")
sc.onkeypress(rpaddledown, "Down")


while True:
    sc.update()
    time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check if ball hits wall
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *=-1
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *=-1
    
    if ball.xcor() > 500:
        ball.goto(0,0)
        bspeed = 5
        ball.dy *= -1
        left_player +=1
        score.clear()
        score.write("{}                           {}".format(left_player, right_player),
            align = "center", font = ("Courier", 24, "normal"))
    if ball.xcor() < -500:
        ball.goto(0,0)
        bspeed = 5
        ball.dy *= -1
        right_player +=1
        score.clear()
        score.write("{}                           {}".format(left_player, right_player),
            align = "center", font = ("Courier", 24, "normal"))
        
    #paddle and ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and \
            (ball.ycor() < right_pad.ycor() + 50 and ball.ycor() > right_pad.ycor() - 50):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and \
            (ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50):
        ball.setx(-360)
        ball.dx *= -1


sc.exitonclick()
