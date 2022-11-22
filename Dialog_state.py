import play_state
import game_framework
from pico2d import *
from Map import Maping
import Font

Diag_log = None

def enter():
    global Diag_log
    Maping[play_state.round].Npc[play_state.hero.Meet_Npc].return_Diag()
    pass

def handle_events():
    global Diag_log
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                Maping[play_state.round].Npc[play_state.hero.Meet_Npc].return_Diag()


def update():
    pass

def draw():
    clear_canvas()

    play_state.draw_world()
    play_state.Board.clip_draw(0, 1, 83, 76, 320, 75, 644, 140)

    Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Draw()
    update_canvas()

    pass

def exit():
    pass

def resume():
    pass

def pause():
    pass