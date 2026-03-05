import turtle
#screen setup
wind = turtle.Screen()
wind.title("Ping Pong game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#player1 specifications
player1 = turtle.Turtle()
player1.speed(0) #animation speed
player1.shape("square")
player1.color("blue")
player1.penup() #no line traces
player1.goto(-350, 0) #initial position
player1.shapesize(stretch_wid=5, stretch_len=1)

#player2 specifications
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("red")
player2.penup()
player2.goto(350, 0)
player2.shapesize(stretch_wid=5, stretch_len=1)

#ball specifications
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.07
ball.dy = 0.07
#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Blue: 0 | Red: 0", align="center", font=("Courier", 24, "normal"))
#moving functions
def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)
    
def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)
    
def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)
    
def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)
    
#keyboard bindings
wind.listen()
wind.onkeypress(player1_up, "w")
wind.onkeypress(player1_down, "s")
wind.onkeypress(player2_up, "Up")
wind.onkeypress(player2_down, "Down")



#gameloop
while True:
    wind.update()
    
    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Blue: {} | Red: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Blue: {} | Red: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
    

        
    