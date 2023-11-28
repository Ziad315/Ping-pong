#import libraries
import turtle

wind=turtle.Screen()  #intialize the screen
wind.title("Ping pong") #make title for this screen
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
rack1.goto(-350,0)    # select postion

#racket two
rack2= turtle.Turtle() 
rack2.speed(0)
rack2.shape("square")
rack2.color("red")
rack2.shapesize(stretch_len=1,stretch_wid=5)
rack2.penup()
rack2.goto(350,0)


#ball
#Game loop
while True:
    wind.update()  #update the windows everytime the loop run

else:
    exit()