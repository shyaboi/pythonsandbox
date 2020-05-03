import turtle 

wn = turtle.Screen()
wn.title('ponglyfe')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# pad a
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

# pad b
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.color('white')
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)


while True:
    wn.update()