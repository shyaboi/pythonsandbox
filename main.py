import turtle 

wn = turtle.Screen()
wn.title('ponglyfe')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.penup()
pad_a.goto(-350,0)

while True:
    wn.update()