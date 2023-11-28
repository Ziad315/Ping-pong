#import libraries
import turtle
import tkinter as tk
from pygame import mixer


wind=turtle.Screen()  #intialize the screen
wind.title("Ping Pong") #make title for this screen
wind.bgcolor("black")    # make background color
wind.setup(width=800,height=600)  #set width and height
wind.tracer(0)   #windows doesnt update itself


#racket one
rack1= turtle.Turtle()  # Make object turtle 
rack1.speed(0)     #control turtle module speed
rack1.shape("square")  # Make turtle shape square
rack1.color("blue")     # male color =blue
rack1.shapesize(stretch_len=1,stretch_wid=5)   # Strech size of square
rack1.penup()  # remove turtle lines
rack1.goto(-350,0)    # select postion in the left  

#racket two
rack2= turtle.Turtle()   #Make object turtle 
rack2.speed(0)
rack2.shape("square")     
rack2.color("red")
rack2.shapesize(stretch_len=1,stretch_wid=5)
rack2.penup()
rack2.goto(350,0)    # Set postion of the turtle in the right side of the screen
 
#ball
ball= turtle.Turtle()   #create ball
ball.speed(0)
ball.shape("circle")   #make ball in circle shape
ball.color("white")    # Make color white
ball.penup()     
ball.goto(0,0)       #Make the ball in the center ot the screen
ball.dx= 0.25         #rate of change in ball direction of x
ball.dy= 0.25         #Rate of change in ball direction of y

#Background music
def play_music():
    mixer.init()
    mixer.music.load('song.mp3') # replace 'your_music_file.mp3' with your music file
    mixer.music.play()


#Score
score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("White")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 : 0   player 2 : 0 ", align="center", font=("Time new roman",16,"normal"))


#Move function

def rack1_moveup():    
    y=rack1.ycor()     #get the y of the first racket
    y+=20
    rack1.sety(y)     #set the new position of racket one

def rack1_movedown():
    y=rack1.ycor()
    y-=20
    rack1.sety(y)



def rack2_moveup():    
    y=rack2.ycor()     #get the y of the second racket
    y+=20
    rack2.sety(y)     #set the new position of racket two


def rack2_movedown():
    y=rack2.ycor()
    y-=20
    rack2.sety(y)    

#keyboard
wind.listen()
play_music()
wind.onkeypress(rack1_moveup,"w")    #When we press w in the keyboard it goes up
wind.onkeypress(rack1_movedown,"s")  #When we press s in the keyboard it goes down
wind.onkeypress(rack2_moveup,"Up")    #When we press UP in the keyboard it goes up
wind.onkeypress(rack2_movedown,"Down")  #When we press DOWN in the keyboard it goes down


#Game loop
while True:
    wind.update()  #update the windows everytime the loop run
    

    ball.setx(ball.xcor()+ball.dx)  #get the x of the ball and add change in x
    ball.sety(ball.ycor()+ball.dy) #get the y of the ball and add change in y

    #Check ball in board 
    if ball.ycor() > 290:      #When the ball it the wall up it reflect
        ball.sety(290)
        ball.dy *=-1



    if ball.ycor() < -290:      #When the ball it the wall it reflect
      ball.sety(-290)
      ball.dy *=-1    


    if ball.xcor() >390:    #When the ball hit right it return to the center
        ball.goto(0,0)  
        ball.dx *=-1
        score1+=1
        score.clear()
        score.write("player 1 : {}  player 2 : {} ".format(score1,score2), align="center", font=("Time new roman",16,"normal"))


    if ball.xcor() <-390:     #When the ball hit left it return to the center
        ball.goto(0,0)  
        ball.dx *=-1
        score2+=1
        score.clear()
        score.write("player 1 : {}  player 2 : {} ".format(score1,score2), align="center", font=("Time new roman",16,"normal"))


    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < rack2.ycor() +50 and ball.ycor() > rack2.ycor()-50):
        ball.setx(340)
        ball.dx*=-1


    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < rack1.ycor() +50 and ball.ycor() > rack1.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        

 
  
 
