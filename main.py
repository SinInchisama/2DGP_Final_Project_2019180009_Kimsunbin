import game_framework
from pico2d import *
import play_state
import logo_state
import Menu_state



open_canvas(640,576)
game_framework.run(play_state)
close_canvas()