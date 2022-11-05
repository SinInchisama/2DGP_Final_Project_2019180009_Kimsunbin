import Choose_Poketmon
from pico2d import *
import game_framework
import play_state
import Battle
import wild_Battle
def enter():
    Choose_Poketmon.enter()

def handle_events():
    global CusorY, frame
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.pop_state()
            elif event.key == SDLK_DOWN:
                if Choose_Poketmon.CusorY + 1 < play_state.hero.Pcount:
                    Choose_Poketmon.CusorY = (Choose_Poketmon.CusorY + 1) % 7
                else:
                    Choose_Poketmon.CusorY = 6
            elif event.key == SDLK_UP:
                if (Choose_Poketmon.CusorY > 0):
                    Choose_Poketmon.CusorY -= 1
            elif event.key == SDLK_a:
                if (Choose_Poketmon.CusorY != 6):
                    if(play_state.hero.pList[Battle.Poket_Order].Hp != 0):
                        if ( play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
                            wild_Battle.Order, wild_Battle.Order_Que, wild_Battle.round = 1, [None], 0
                    play_state.hero.pList[Battle.Poket_Order].del_Change_ability()
                    Battle.Poket_Order = Choose_Poketmon.CusorY
                    play_state.hero.pList[Choose_Poketmon.CusorY].init_Change_ability()
                    game_framework.pop_state()
                    # frame = 645       # 포켓몬 선택하고 무슨 행동할지 선택하는 창
                elif (Choose_Poketmon.CusorY == 6):
                    game_framework.pop_state()
    pass

def draw():
    Choose_Poketmon.draw()

def update():
    Choose_Poketmon.update()

def exit():
    pass

def resume():
    pass

def pause():
    pass