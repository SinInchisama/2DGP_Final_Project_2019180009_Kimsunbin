from pico2d import *
import game_framework
import play_state
import Choose_Poketmon
import Throw_Ball
import wild_Battle

Cursory = None
Cursoyx = None
Minusx,Minusy = 0,0
Cursor_image,Escape = None,None

def enter():
    global Cursoyx,Cursory,Cursor_image
    Cursor_image = load_image('./resource/image/Cursor.png')
    Cursoyx, Cursory = 0,0
    pass

def handle_events():
    global Cursory,Cursoyx,Escape
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_ESCAPE:
                game_framework.pop_state()
                Escape = 'Escape'
            elif event.key == SDLK_LEFT:
                Cursoyx -=1
                if(Cursoyx == -1):
                    Cursoyx = 3
                Cursory = 0
            elif event.key == SDLK_RIGHT:
                Cursoyx = (Cursoyx + 1) %4
                Cursory = 0
            elif event.key == SDLK_UP:
                Cursory -= 1
                if(Cursory == -1):
                    Cursory = 3
                pass
            elif event.key == SDLK_DOWN:
                Cursory = (Cursory+1)%4
                if(Cursoyx == 2):
                    Cursory = Cursory % 2
                pass
            elif event.key == SDLK_a:
                if(Cursoyx == 0):
                    if(play_state.hero.inventory.Heal[Cursory][1] != 0):
                        play_state.hero.inventory.Nowtype = 0
                        play_state.hero.inventory.Nowitem = Cursory
                        game_framework.change_state(Choose_Poketmon)
                if (Cursoyx == 1):
                    if(play_state.hero.inventory.Use_type == 'Use_battle' and wild_Battle.Battle_type == 'Wild'):
                        if (play_state.hero.inventory.Ball[Cursory][1] != 0):
                            play_state.hero.inventory.Nowitem = Cursory
                            play_state.hero.inventory.Ball[play_state.hero.inventory.Nowitem][1] -= 1
                            game_framework.change_state(Throw_Ball)
                            wild_Battle.Push_type = 'Throw_Ball'
                if (Cursoyx == 2):
                    if play_state.hero.inventory.Use_type != 'Use_battle':
                        if play_state.hero.inventory.Spray[Cursory][1] != 0:
                            play_state.hero.step += play_state.hero.inventory.Spray[Cursory][0].Use_daily()
                            play_state.hero.inventory.Spray[Cursory][1] -= 1
                            game_framework.pop_state()
                    pass
                pass
    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.hero.inventory.Draw(Cursoyx,Cursory)
    Cursor_image.clip_draw(0,0,32,32,170,500 - (Cursory*70),16,16)
    delay(0.02)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    if(Escape != None):
        play_state.hero.inventory.Use_type = ''
    pass