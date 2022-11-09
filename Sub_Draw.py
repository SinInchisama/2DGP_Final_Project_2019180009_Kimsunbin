import play_state
from pico2d import *

Emergence = None

def Init_SubDraw():
    global Emergence
    Emergence = load_image('./resource/image/emergence.png')


def Emergence(i):
    Emergence = load_image('./resource/image/emergence.png')


    clear_canvas()
    play_state.draw_world()
    Emergence.clip_draw(8 + (i%5)*161,1335 - (i//5)*145,160,144,320,288,640,576)
    update_canvas()

