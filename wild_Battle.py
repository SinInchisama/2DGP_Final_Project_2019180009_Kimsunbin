from pico2d import *
import play_state
import Poketmon
from random import randint

import game_framework

select_Poketmon,wild_Poketmon = None,None
rand = randint

def enter():
    global select_Poketmon,wild_Poketmon
    if(play_state.round == 1):
        select_Poketmon = [9,11,14,17,22,24]
        wild_Poketmon = Poketmon.Tr_Poketmon(select_Poketmon[rand(0,len(select_Poketmon)-1)],rand(3,10),0)
        wild_Poketmon.Set_ability()
        pass
    else:
        pass
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_x:
                game_framework.pop_state()
    pass


def update():
    print(wild_Poketmon.Pattack,wild_Poketmon.level)
    pass


def draw():
    pass