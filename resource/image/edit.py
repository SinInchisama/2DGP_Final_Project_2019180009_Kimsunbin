from pico2d import *

open_canvas(1200,900)

map = load_image('First_gym.png')

map.clip_draw(8,16,640,576,600,450)
update_canvas()
delay(5)

close_canvas()
