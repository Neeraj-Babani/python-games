#PongGame
from fileinput import close
import turtle
win=turtle.Screen()
win.title("Pong Game")
win.bgcolor("black") 
win.setup(width=800,height=600)
win.tracer(0)
#paddle A
paddleA=turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-375,0)

#paddle B
paddleB=turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(375,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.25
ball.dy=.25

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player 1: 0  player 2: 0",align="center",font=("Courier",24,"normal"))

#score
scoreA=0
scoreB=0

#function  for paddle A to go up
def paddleA_up():
    y=paddleA.ycor()
    paddleA.dy= 20
    paddleA.sety(paddleA.ycor()+paddleA.dy)
#function  for paddle A to go down
def paddleA_down():
    y=paddleA.ycor()
    paddleA.dy= -20
    paddleA.sety(paddleA.ycor()+paddleA.dy)
#function  for paddle b to go up
def paddleB_up():
    y=paddleB.ycor()
    paddleB.dy= 20
    paddleB.sety(paddleB.ycor()+paddleB.dy)
#function  for paddle A to go down
def paddleB_down():
    y=paddleB.ycor()
    paddleB.dy= -20
    paddleB.sety(paddleB.ycor()+paddleB.dy)
#keyboard binding
win.listen()
win.onkeypress(paddleA_up,"w")
win.onkeypress(paddleA_down,"s")
win.onkeypress(paddleB_up,"Up")
win.onkeypress(paddleB_down,"Down")

#Main game Loop
while True:
    win.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreA+=1
        pen.clear()
        pen.write("player 1: {}  player 2: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))

    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx*=-1
        scoreB+=1
        pen.clear()
        pen.write("player 1: {}  player 2: {}".format(scoreA,scoreB),align="center",font=("Courier",24,"normal"))
        
    #border checking for paddles
    if paddleA.ycor()> 290:
        paddleA.sety(-280)
    if paddleA.ycor()< -290:
        paddleA.sety(280)
    if paddleB.ycor()> 290:
        paddleB.sety(-280)
    if paddleB.ycor()< -290:
        paddleB.sety(280)
    
    #paddle and ball collisions
    if(ball.xcor()>365 and ball.xcor()<385)  and (ball.ycor()<paddleB.ycor() + 40 and ball.ycor()>paddleB.ycor()-40):
        ball.setx(365)
        ball.dx*=-1
    if(ball.xcor()<-365 and ball.xcor()> -385)  and (ball.ycor()<paddleA.ycor() + 40 and ball.ycor()>paddleA.ycor()-40):
        ball.setx(-365)
        ball.dx*=-1