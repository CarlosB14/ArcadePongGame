import turtle

def window_setup():
    window = turtle.Screen()
    window.title("Super-Pong")
    window.bgcolor("purple")
    window.setup(width=800, height=600)
    window.tracer(0)
    return window


def left_paddle_config():
    left_paddle = turtle.Turtle()
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("pink")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-350, 0)
    return left_paddle


def right_paddle_config():
    right_paddle = turtle.Turtle()
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("red")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(350, 0)
    return right_paddle

def ball_config():
    ball = turtle.Turtle()
    ball.speed(2)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.5
    ball.dy = -0.5
    return ball