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
        pass
    else:
        select_Poketmon = [10, 13, 16, 18,20, 23, 25]
        wild_Poketmon = Poketmon.Tr_Poketmon(select_Poketmon[rand(0, len(select_Poketmon) - 1)], rand(10, 20), 0)
        pass
    wild_Poketmon.Set_ability()
    wild_Poketmon.Set_Skill()
    for i in play_state.hero.pList[0].Skill_List:
        print(i)
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
    pass


def draw():
    clear_canvas()
    play_state. Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)
    Poketmon.Poket_Data[wild_Poketmon.Num].Front_Draw(500,450,224,224)
    Poketmon.Poket_Data[play_state.hero.pList[0].Num].Back_Draw(120, 200, 224, 224)
    update_canvas()
    pass