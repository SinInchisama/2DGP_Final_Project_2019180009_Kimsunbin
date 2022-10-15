from pico2d import *
import game_framework
import play_state

Choose_image = None
Cursor_image = None
CusorY = None
frame = None

def enter():
    global Menu_image,CusorY,Cursor_image,frame
    Menu_image = load_image('./resource/image/Choose_Poketmon.png')
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    frame = 0
    pass

def handle_events():
    global CusorY,frame
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.pop_state()
            elif event.key == SDLK_DOWN:
                CusorY = (CusorY + 1) % 7
            elif event.key == SDLK_a:
                if (CusorY == 0):
                    frame = 645
                elif(CusorY == 6):
                    game_framework.pop_state()
def draw():
    pass

def update():
    clear_canvas()
    Menu_image.clip_draw(5 + frame,7,640,576,320,288)
    Cursor_image.clip_draw(0, 0, 32, 32, 15, 525 - (64 * CusorY))
    update_canvas()
    pass

def exit():
    pass

def pause():
    pass