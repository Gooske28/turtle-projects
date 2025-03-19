import turtle
t = turtle.Turtle()
t.pensize(1)
t.speed(10)
colors = ["red", "green", "blue"]

for i in range(36):
  for _ in range(3):
    t.pencolor(colors[i % 3])
    t.forward(200)
    t.right(120)
  t.right(10)