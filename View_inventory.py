from pico2d import *
import game_framework
import play_state

Cursory = None
Cursoyx = None
Minusx,Minusy = 0,0

def enter():
    global Cursoyx,Cursory
    Cursoyx, Cursory = 0,0
    pass

def handle_events():
    global Cursory,Cursorx
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_LEFT:
                Cursorx -=1
                if(Cursorx == -1):
                    Cursorx = 3
            elif event.key == SDLK_RIGHT:
                Cursorx = (Cursorx + 1) %4
            elif event.key == SDLK_LEFT:
                pass
            elif event.key == SDLK_RIGHT:
                pass
            elif event.key == SDLK_a:
                print(play_state.hero.inventory.x,play_state.hero.inventory.y)
    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.hero.inventory.Draw(Cursory)
    delay(0.02)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    pass