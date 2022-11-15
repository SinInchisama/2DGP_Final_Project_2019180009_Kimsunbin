from pico2d import *
import game_framework
import play_state

Cursory = None
Cursoyx = None

def enter():
    global Cursoyx,Cursory
    Cursoyx, Cursory = 0,0
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_ESCAPE:
                game_framework.pop_state()
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