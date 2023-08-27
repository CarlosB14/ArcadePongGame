'''
Configuration of movements of the paddles
Input --> Paddle configuration right and left
'''

def left_move_up(left_paddle):
        y = left_paddle.ycor()
        if y < 250:
            y += 20
        return left_paddle.sety(y)

def left_move_down(left_paddle):
        y = left_paddle.ycor()
        if y > -240:
            y -= 20
        return left_paddle.sety(y)

def right_move_up(right_paddle):
        y = right_paddle.ycor()
        if y < 250:
            y += 20
        return right_paddle.sety(y)

def right_move_down(right_paddle):
        y = right_paddle.ycor()
        if y > -240:
            y -= 20
        return right_paddle.sety(y)
def keyboard_setting(left_paddle, right_paddle, window):
    window.listen()
    window.onkeypress(lambda: left_move_up(left_paddle), "w")
    window.onkeypress(lambda: left_move_down(left_paddle), "s")
    window.onkeypress(lambda: right_move_up(right_paddle), "Up")
    window.onkeypress(lambda: right_move_down(right_paddle), "Down")