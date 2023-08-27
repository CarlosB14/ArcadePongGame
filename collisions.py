import time
'''
We configure the collisions of the ball
Input--> Ball and paddles
'''

def check_collision_paddles(ball, left_paddle, right_paddle):
    if (
        (ball.dx > 0) and
        (350 > ball.xcor() > 340) and
        (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50)
    ):
        ball.color("green")
        ball.setx(340)
        ball.dx *= -1

    elif (
        (ball.dx < 0) and
        (-350 < ball.xcor() < -340) and
        (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50)
    ):
        ball.color("green")
        ball.setx(-340)
        ball.dx *= -1


def collision_top_bottom_walls(ball):
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

# --- Returns the ball to the center ---
def collision_left_right_wall(ball):
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        time.sleep(2)
        
