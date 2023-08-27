from collisions import check_collision_paddles, collision_top_bottom_walls, collision_left_right_wall 
def main_game_loop(ball, right_paddle, left_paddle, window):
    while True:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        check_collision_paddles(ball, left_paddle, right_paddle)

        collision_top_bottom_walls(ball)

        collision_left_right_wall(ball)
