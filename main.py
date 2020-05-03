import turtle 
import winsound

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
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.color('white')
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = .1
ball.dy = -.1


# Score Card
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Playa Left: 0 Playa Right: 0', align='center', font=('Courier', 24, 'normal'))

# Score Function
score_a = 0
score_b = 0


# function

    # player 1
def pad_a_up():
    y = pad_a.ycor()
    y += 25
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y += -25
    pad_a.sety(y)
    
    
    # player 2

def pad_b_up():
    y = pad_b.ycor()
    y += 25
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y += -25
    pad_b.sety(y)
# Keyboard Bindings

wn.listen()
# player 1
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
# player 2
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")


# game looop
while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #boarder check

        # top boarder
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("shyaboi.wav", winsound.SND_ASYNC)
        # bottom boarder
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("shyaboi.wav", winsound.SND_ASYNC)
        # right "goal"
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("jayz_yessir.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Playa Left: {}  Playa Right: {} ".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

      # left "goal"
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("business-man.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Playa Left: {}  Playa Right: {} ".format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))


# paddle and ball collision
            # pad a
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("shyaboi.wav", winsound.SND_ASYNC)

        
            # pad b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("shyaboi.wav", winsound.SND_ASYNC)