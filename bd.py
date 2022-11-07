

import turtle
import  time
import  math

def draw_square():
    side = 200
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    turtle.forward(side)
    turtle.left(90)
    
    
    
def draw_circle():

  redius = 50
  
  turtle.circle(redius)
  
  

turtle.fillcolor('green')
turtle.begin_fill()
draw_square()
turtle.end_fill()
turtle.penup()
turtle.setpos(100,60)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
draw_circle()
turtle.end_fill()
turtle.penup()


time.sleep(3)

turtle.clear()

