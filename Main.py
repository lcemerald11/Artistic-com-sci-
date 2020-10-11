import turtle as trtl

painter = trtl.Turtle()
  # This draws out the base of a tree. U can selsect the starting cords and the scale (0.5-2)
def tree(x_val,y_val,scale):
  # This draws out the base of a tree. U can selsect the starting cords and the scale (0.5-2)
  painter.color("brown")
  painter.penup()
  painter.pendown()
  painter.goto(x_val, y_val)
  count = 0

  painter.fillcolor("brown")
  painter.begin_fill()
  while count <= 4:

    if count % 2 == 0:
        painter.forward(3*scale)
        print(count,3*scale)
        painter.right(90)
    else:
        painter.forward(6*scale)
        painter.right(90)
    count += 1
  painter.end_fill()

  painter.fillcolor("green")
  painter.penup()
  painter.goto(x_val, y_val)
  painter.goto ( (x_val - (1.5*scale) ), ( y_val + (6*scale)+(11*scale) ) )
  painter.pendown()
  painter.color("green")
  print(painter.xcor())
  painter.setheading(180)
  painter.begin_fill()
  painter.circle((9*scale),360,3)
  painter.end_fill()


# Drawing mountain
painter.fillcolor("gray")
painter.penup()
painter.goto(0,350)
painter.pendown()
painter.begin_fill()
painter.setheading(180)
painter.circle(1000,360,3)
painter.end_fill()

#Draws Icecap at top of mountain
painter.fillcolor("white")
painter.penup()
painter.goto(0,350)
painter.pendown()
painter.begin_fill()
painter.setheading(180)
painter.circle(100,360,3)
painter.end_fill()
tree(2.5, 350, 2)


#Drawing hills using half circles and while loop
counterHill = 0
Hill_x = -250
while counterHill < 5:
    if (counterHill % 2) == 0:
        radi = 100
    else:
        radi = 150
    painter.fillcolor("green")
    painter.penup()
    painter.goto(Hill_x,-400)
    print(Hill_x)
    painter.pendown()
    painter.begin_fill()
    painter.setheading(90)
    painter.circle(radi,180)
    painter.end_fill()
    counterHill += 1
    if (counterHill % 2) == 0:
        Hill_x += 150
    else:
        Hill_x += 200


wn = trtl.Screen()
wn.mainloop()
