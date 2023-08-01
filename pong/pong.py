from asyncore import write
import turtle
import winsound

win = turtle.Screen() # creates the window
win.title("Pong") # title of the screen
win.bgcolor("blue") # backcolor of the screen
win.setup(width=800, height=600)
win.tracer(0) # stops the window from updating


#Score
score_1 = 0
score_2 = 0 

#Player1
player_1 = turtle.Turtle()
player_1.speed(0)# the speed for animation..maximum speed
player_1.shape("square") # shape of player 1
player_1.color("white") # color of player 1
player_1.shapesize(stretch_wid=6, stretch_len=1) # stretches player 1
player_1.penup()
player_1.goto(-350,0) # thats is the starting postion of player 1


#Player2
player_2 = turtle.Turtle()
player_2.speed(0)# the speed for animation..maximum speed
player_2.shape("square") # shape of player 2
player_2.color("white") # color of player 2
player_2.shapesize(stretch_wid=6, stretch_len=1) # stretches player 2
player_2.penup()
player_2.goto(350,0) # thats is the starting postion of player 2

#Ball
ball = turtle.Turtle()
ball.speed(0)# the speed for animation..maximum speed
ball.shape("circle") # shape of ball
ball.color("white") # color of ball
ball.penup()
ball.goto(0,0) # that is the starting position of the ball
ball.dx = 0.2 # Every time the ball moves, it moves by 2 pixels
ball.dy = 0.2

#pen
pen = turtle.Turtle()
pen.speed(0) #that is the animation speed
pen.color("white")
pen.penup() # it doesnt draw a line between those two point
pen.hideturtle() # it hides the pen
pen.goto (0, 260) # were the scores will be written
pen.write("Player 1: 0 Player 2: 0", align ="center", font=("Courier", 24, "normal"))

#FUNCTION
#for player 2
def player_1_up(): # it is used to define the function upwards for player 1
    y = player_1.ycor() # it returns the y codinatate and assign it to a variable called y
    y +=20 # Adds 20 pixels to the y coordinate upwards
    player_1.sety(y) # calculate the y coordinate

def player_1_down(): # it is used to define the function downwards for player 1
    y = player_1.ycor() # it returns the y codinatate and assign it to a variable called y
    y -=20 # Adds 20 pixels to the y coordinate downwards
    player_1.sety(y) # calculate the y coordinate

#for player 2
def player_2_up(): # it is used to define the function upwards for player 2
    y = player_2.ycor() # it returns the y codinatate and assign it to a variable called y
    y +=20 # Adds 20 pixels to the y coordinate upwards
    player_2.sety(y) # calculate the y coordinate

def player_2_down(): # it is used to define the function downwards for player 2
    y = player_2.ycor() # it returns the y codinatate and assign it to a variable called y
    y -=20 # Adds 20 pixels to the y coordinate downwards
    player_2.sety(y) # calculate the y coordinate

#Keyboard binding
#for player 1
win.listen() # it tells the module to listen for keyboard inputs for player 1
win.onkeypress(player_1_up, "w") # when the user press "w", it calls the function player_1_up

win.listen() # it tells the module to listen for keyboard inputs for player 1
win.onkeypress(player_1_down, "s") # when the user press "s", it calls the function player_1_down

#for player 2
win.listen() # it tells the module to listen for keyboard inputs for player 2
win.onkeypress(player_2_up, "Up") # when the user press "Up arrow key", it calls the function player_2_up

win.listen() # it tells the module to listen for keyboard inputs for player 2
win.onkeypress(player_2_down, "Down") # when the user press "Down arrow key", it calls the function player_2_down


#Main game loop
while True:
    win.update() # everytime the loop runs, it updates the screen


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290: # if the ball is in postion of y > 290
        ball.sety(290) # set it back to 290
        ball.dy *= -1 # it ""reverses the direction 
       # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290: # if the ball is in postion of y < -290
        ball.sety(-290) # set it back to 290
        ball.dy *= -1 # it reverses the 
        
    if ball.xcor() > 390: # if the ball is in postion of x > 390
        ball.goto(0, 0) # set it back to the center
        ball.dx *= -1 # it reverses the direction
        score_1 += 1 # increase the score of the player by 1
        pen.clear() # it clears the previous score before a new one is written
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2),align ="center", font=("Courier", 24, "normal"))

       
    if ball.xcor() < -390: # if the ball is in postion of x > 390
        ball.goto(0, 0) # set it back to the center
        ball.dx *= -1 # it reverses the direction
        score_2 += 1 # increase the score of the player by 1
        pen.clear() # it clears the previous score before a new one is written
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2),align ="center", font=("Courier", 24, "normal"))

       
 #Player and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 40 and ball.ycor() > player_2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 40 and ball.ycor() > player_1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
   
    
