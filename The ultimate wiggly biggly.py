import turtle
t = turtle.Turtle()
t.speed(0)
def wigglybiggly(x,y,f):
  t.penup()
  t.setpos(x,y)
  t.pendown()
  for i in range(6):
    t.forward(f)
    t.left(60)

def crazytime():
  for i in range(60):
    wigglybiggly(0,0,i+5)
def cool():
  for i in range(60):
    crazytime()
def uwu():
  for i in range(60):
    cool()
    
cool()