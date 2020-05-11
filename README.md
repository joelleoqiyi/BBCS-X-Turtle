# Lightning Turtles?

Turtles are slow :turtle:... What if we add a bolt of lightning to it in a lab?

This Lighting Lab is happening online on Fri 15 May - 1110 to 1120. In this Lightning Lab, you will be learning and experimenting with the [turtle](https://docs.python.org/3/library/turtle.html) python library. This lab would be 10 mins long and is split into 2 sections.
- For the first section (5mins), you will be **viewing a 5 min workshop video that will go through the basics of turtle.py**
- For the second section (5mins), you will need to use **turtle.py** to draw a drawing and submit your drawing to [https://tinyurl.com/bbcs20lightningturtle](https://tinyurl.com/bbcs20lightningturtle).
  * While drawing, you would need to adhere to the central theme of (ENTER THEME HERE)
  * But what exactly is the picture/diagram that you draw is **entirely up to you**. You can draw pictures as simple as a rectangle or as complex as a map of singapore :laughing:

## The Theme for this lighting lab is...
**(ENTER THEME HERE ON THAT DAY)**

## Submittables:  
1) your drawings (made using turtle.py)
2) an explanation (in 100 words or less) why your drawing fulfils/matches the theme given.
3) python code which you used to draw the drawing

## Some things to take note:
1) You can either submit links (for eg: repl.it links) OR upload the image/txt/python files itself
2) You can either work in pairs or individually
3) Successful submissions with logical explanations would get extra chances for Day 2's Lucky Draw.
4) Standard Code of Conduct, NO direct plagiarism from anywhere. (Googling is allowed)
5) There is no limit to the amount of times you can submit (but no spamming entries please!)

NOTE: For a submission considered as successful, you have to submit BEFORE 1120 and have all 3 submittables.(submissions after stipulated ending time would be judged on a case-by-case basis, for eg: if you have a wifi issue, etc)

---

## SECTION 0: Let's start...

- If you are participating in the lightning lab, you should have **already downloaded some kind of Python IDE** such as [IDLE](https://www.python.org/downloads/). *If you have not, you can use online compilers such as [Repl.it](https://repl.it/languages/python_turtle) but do note (after some ~~intensive~~ testing), you might face some compile issues while using online compilers and hence will have problems with running certain codes especially from SECTION 3 Onwards*

---

## SECTION 1: Customising your turtle...

- By default when you installed python, the turtle library is already installed but you would import the turtle library into your code such that you can use it later on:
```
import turtle
from turtle import *
```
- Now, we need to create the turtle object or simply the "turtle" using the .Turtle() method from the turtle library:
```
t = turtle.Turtle() #note: t is just a random variable, you can replace it with anything you wish (except for turtle)
```
- If you want to create multiple "turtles", simply call the `.Turtle()` method as many times as you need but assign it to a different variable each time
```
#code below creates 2 "turtles"
t = turtle.Turtle()
k = turtle.Turtle()
```
- But if you click run now (on your IDE or online compiler), you will realise that you get an arrowhead instead of a turtle?? That's because by default the shape of the "turtle" is an arrowhead. Let's change it to a turtle using the `.shape()` method of the turtle object :laughing::
```
t.shape("turtle")
#note: since .shape() is a method of the turtle object you created, you need to prepend the variable which you assigned the turtle object to.
#you can also try it out with these shapes “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
```
- Let's now change the color of your turtle (and whatever it draws) using the `.color()` method of the turtle object:
```
t.color("red") #change the value in the brackets to the color of your choosing
```
- Finally, let's change the size of the line which our "turtle" draws using the `.pensize()` method of the turtle object:
```
t.pensize(5) #the larger the number in the bracket, the thicker the line
```
---

## SECTION 2: Moving your turtle...

- Now, let's move our "turtle" forward/backwards. If you look closely, by default, the turtle is facing in the rightward direction. Hence, we can use the `.forward()` and `.backward()` method to move forward and backward (respectively) in the direction which the turtle is facing. The number in the brackets specify the distance which the turtle moves
```
t.forward(100) #moves the turtle forward by 100 pixels therefore drawing a line of 100 pixels
t.backward(200) #moves the turtle back by 200 pixels therefore drawing a line of 200 pixels
```
- Now, how about if we want to turn our turtle (relative to the direction which the turtle is facing), we can use the `.left()` and `.right()` method to turn our turtle anticlockwise and clockwise (respectively). The number in the brackets specify the angle in which the turtle turns
```
t.left(90) #turns anticlockwise by 90 degrees
t.right(123) #turns clockwise by 123 degrees
```
- What if we want to move our turtle around without it drawing any lines? We can use the `.penup()` method to stop our turtle from drawing until we call the `.pendown()` method, after which our turtle would start drawing again.
```
t.penup() #turtle stops drawing
t.forward(100) #turtle doesn't draw line
t.pendown() #turtle starts drawing again
t.forward(100) #turtle draws line
```
- What if we want our turtle to move faster (for that dramatic wow effect!) We can use the `.speed()` method to control the speed in which our turtle moves. The larger the number in the brackets is, the faster our turtle moves. Note: `.speed(0)` is an exception as it makes the turtle "teleport":
```
t.speed(1) #moves slower than t.speed(100)
```

---

# Queries:
For queries, please contact @lightninglabs_turtle in the #workshop-help Discord channel!
