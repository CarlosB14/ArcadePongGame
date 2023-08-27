from utils_turtle import window_setup, left_paddle_config, right_paddle_config, ball_config
from keyboard_setting import keyboard_setting
from main_game_loop import main_game_loop

window = window_setup()

left_paddle = left_paddle_config()

right_paddle = right_paddle_config()

ball = ball_config()

keyboard_setting(left_paddle, right_paddle, window)

main_game_loop(ball, right_paddle, left_paddle, window)