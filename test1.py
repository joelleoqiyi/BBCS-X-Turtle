import turtle
from turtle import *
import random 

t = turtle.Turtle()
'''
t.shape("turtle")
t.color("red")
t.pensize(5)

t.forward(100) #count in pixels 
t.backward(200)
t.left(90) #move left by how many angles
t.penup()
t.backward(200)
t.pendown()
t.color("green")
t.right() #move right by how many angles


#how to move at the same time?
t.speed(1) #speed of the turtle :) max speed = speed = 0 

#how to fill in shapes :) 
t.color("red", "blue") #red is outline color, blue is fill color 

t.begin_fill()
t.circle(50) #dont have for rectangle etc. 
t.end_fill() #fills in the shape it just draw. 


for x in range(4): #draw rectangle
  t.forward(100)
  t.right(90)

t.setpos(-200,-150) #set position based on cartesian plane --> two parameters


#draw random circles 
for x in range(5):
  rand1 = random.randrange(-300, 300)
  rand2 = random.randrange(-300, 300)
  t.penup() #move to pos without drawing 
  t.setpos((rand1, rand2))
  t.pendown()
  t.begin_fill()
  t.circle(random.randrange(0,80))
  t.end_fill()

'''
colors = ["black", "blue", "yellow"]
def up():
  t.setheading(90) #90 is north
  t.forward(100)

def down():
  t.setheading(270) #270 is south
  t.forward(100)


def left():
  t.setheading(180) #180 is left
  t.forward(100)

def right():
  t.setheading(0) #0 is left
  t.forward(100)

def clickleft(x,y):
  t.color(random.choice(colors))

def clickright(x,y):
  t.stamp() #stamp down like a stamp :) 

turtle.listen() #listens to input from user , mouse, keyboard

turtle.onscreenclick(clickleft, 1) #can replace 1 with 2 if wan middle mouse button, if replace with 3, means need click right mouse button

turtle.onclick(clickright, 3) #onclick ==> on turtle, onscreenclick ==> anywhere else 
turtle.onkey(up, "Up") #listen to the 2nd parameter and do the function in the first 
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop() #keep continuing to look for the key presses until we exit the code. if dh, then the second we open the program, the turtle would listen once. and end the program. essentially looping ur code. 
#mainloop() can be in a function but also in the main code 
