import Map
from pico2d import *

open_canvas(640,576)

Map.init_map()

while True:
    clear_canvas()
    Map.Draw_Map(7)
    update_canvas()
    delay(0.01)
    get_events()
