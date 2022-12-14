from pico2d import *
import game_framework
import play_state
import Choose_Poketmon
import View_PokeDex_state
import View_inventory

Menu_image = None
Cursor_image = None
CusorY = None

def enter():
    global Menu_image,CusorY,Cursor_image,frame
    Menu_image = load_image('./resource/image/menu_state.png')
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    pass

def handle_events():
    global  CusorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                CusorY = (CusorY + 1) % 4

            elif event.key == SDLK_UP:
                CusorY = CusorY - 1
                if CusorY == -1:
                    CusorY = 3
            elif event.key == SDLK_ESCAPE:
                game_framework.pop_state()

            elif event.key == SDLK_a:
                if CusorY == 0:
                    game_framework.push_state(View_PokeDex_state)
                    pass
                elif CusorY == 1:
                    if(len(play_state.hero.pList)>0):
                        game_framework.push_state(Choose_Poketmon)
                        play_state.hero.type = 'Daily'
                    pass
                elif CusorY == 2:
                    play_state.hero.inventory.Use_type = 'Use_daily'
                    game_framework.push_state(View_inventory)
                    pass
                elif CusorY == 3:
                    game_framework.pop_state()

def update():
    clear_canvas()
    play_state.draw_world()
    Menu_image.clip_draw(0,0,640,576,320,288)
    Cursor_image.clip_draw(0,0,32,32,360,496 - (64 * CusorY))
    update_canvas()
    pass

def draw():
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass