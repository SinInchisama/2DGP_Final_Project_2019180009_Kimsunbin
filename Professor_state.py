from pico2d import *
import game_framework
import play_state

back_image = None
ch_image = None
xframe,yframe = None,None

def enter():
    global back_image,ch_image,xframe,yframe,ch
    xframe, yframe =0,0
    back_image = load_image('./resource/image/1.png')
    ch_image= load_image('./resource/image/Professor_state.png')

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def update():
    global xframe,yframe
    xframe = (xframe + 0.5) % 8
    yframe = (yframe + 0.125)

    if yframe == 3:
        game_framework.change_state(play_state)


def draw():
    global xframe,yframe
    clear_canvas()
    back_image.clip_draw(0, 0, 640, 576, 320, 288)
    ch_image.clip_draw(16 + (128 * int(xframe)), 658 - (257 * int(yframe)), 112 , 110, 311, 317)
    update_canvas()
    delay(0.1)
    pass

def exit():
    pass