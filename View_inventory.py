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
    global Cursory,Cursoyx
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_LEFT:
                Cursoyx -=1
                if(Cursoyx == -1):
                    Cursoyx = 3
            elif event.key == SDLK_RIGHT:
                Cursoyx = (Cursoyx + 1) %4
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
    play_state.hero.inventory.Draw(Cursoyx)
    delay(0.02)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    pass