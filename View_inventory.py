from pico2d import *
import game_framework
import play_state
import Choose_Poketmon

Cursory = None
Cursoyx = None
Minusx,Minusy = 0,0
Cursor_image = None

def enter():
    global Cursoyx,Cursory,Cursor_image
    Cursor_image = load_image('./resource/image/Cursor.png')
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
            elif event.key == SDLK_UP:
                Cursory -= 1
                if(Cursory == -1):
                    Cursory = 3
                pass
            elif event.key == SDLK_DOWN:
                Cursory = (Cursory+1)%4
                pass
            elif event.key == SDLK_a:
                if(Cursoyx == 0):
                    if(play_state.hero.inventory.Heal[Cursory][1] != 0):
                        play_state.hero.inventory.Nowtype = 0
                        play_state.hero.inventory.Nowitem = Cursory
                        game_framework.change_state(Choose_Poketmon)
                pass
    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.hero.inventory.Draw(Cursoyx)
    Cursor_image.clip_draw(0,0,32,32,170,500 - (Cursory*70),16,16)
    delay(0.02)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    play_state.hero.inventory.Use_type = ''
    pass