import turtle as trtl

painter = trtl.Turtle()
def tree(x,y,scale):
  # This draws out the base of a tree. U can selsect the starting cords and the scale (0.5-2)
  painter.color("brown")
  painter.goto(x, y)
  count = 0

  painter.fillcolor("brown")
  painter.begin_fill()
  while count <= 4:

    if count % 2 == 0:
        painter.forward(3*scale)
        painter.right(90)
    else:
        painter.forward(6*scale)
        painter.right(90)
    count += 1
  painter.end_fill()

  painter.fillcolor("green")
  painter.color("green")
  painter.begin_fill()
  painter.goto((x+1.5*scale), (y + 14*scale))
  painter.setheading(180)
  painter.circle((9*scale),360,3)
  painter.end_fill()



tree(1, 2, 2)
wn = trtl.Screen()
wn.mainloop()
