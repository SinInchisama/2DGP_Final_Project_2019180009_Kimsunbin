import game_framework
from pico2d import *
import play_state
import logo_state

open_canvas(640,576)
game_framework.run(logo_state)
close_canvas()