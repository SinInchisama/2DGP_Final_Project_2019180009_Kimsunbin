from pico2d import *
import game_framework
import Status_state
import play_state

Choose_image = None
Cursor_image = None
CusorY = None
frame = None
Pframe = None

def enter():
    global Menu_image,CusorY,Cursor_image,frame,Pframe
    Menu_image = load_image('./resource/image/Choose_Poketmon.png')
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    frame = 0
    Pframe = 0
    pass

def handle_events():
    global CusorY,frame
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.pop_state()
            elif event.key == SDLK_a:
                game_framework.push_state(Status_state)
            elif event.key == SDLK_DOWN:
                if CusorY + 1 < play_state.hero.Pcount:
                    CusorY = (CusorY + 1) % 7
                else:
                    CusorY = 6
            elif event.key == SDLK_UP:
                if(CusorY >0):
                    CusorY-= 1
            elif event.key == SDLK_a:
                if (CusorY == 0):
                    frame = 645
                elif(CusorY == 6):
                    game_framework.pop_state()
def draw():
    clear_canvas()
    Menu_image.clip_draw(5 + frame, 7, 640, 576, 320, 288)
    Cursor_image.clip_draw(0, 0, 32, 32, 15, 525 - (64 * CusorY))
    for i in range(0,play_state.hero.Pcount):
        play_state.hero.character_image.clip_draw(220 + (int(Pframe) * 35),610,36,36,45,525- (64 * i))
    update_canvas()
    pass

def update():
    global Pframe
    Pframe = (Pframe + 0.01) % 2
    pass

def exit():
    pass

def pause():
    pass