from pico2d import *
import play_state
import Poketmon
from random import randint

import game_framework

select_Poketmon,wild_Poketmon = None,None
select_M = None                             # 현재 커서 위치(메뉴선택과 스킬선택할 때 사용.
Menu_Bool,Skill_Bool = None,None            # 메뉴선택, 스킬선택
rand = randint

def enter():
    global select_Poketmon,wild_Poketmon,select_M,Menu_Bool,Skill_Bool
    if(play_state.round == 1):
        select_Poketmon = [9,11,14,17,22,24]                    # 29번 도로에서 위 도감 번호 포켓몬 중
        wild_Poketmon = Poketmon.Tr_Poketmon(select_Poketmon[rand(0,len(select_Poketmon)-1)],rand(3,10),0)  # 랜덤 포켓몬 생성
        pass
    else:
        select_Poketmon = [10, 13, 16, 18,20, 23, 25]           # 31번 도로
        wild_Poketmon = Poketmon.Tr_Poketmon(select_Poketmon[rand(0, len(select_Poketmon) - 1)], rand(10, 20), 0)
        pass
    wild_Poketmon.Set_ability()                                 # 야생 포켓몬 능력치 세팅
    wild_Poketmon.Set_Skill()                                   # 야생 포켓몬 스킬 분배

    del (select_Poketmon)                                       # 필요 없어진 배열 삭제.
    select_M = 0
    Menu_Bool, Skill_Bool = False,False
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    global Menu_Bool,Skill_Bool

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                if(Menu_Bool == False):             # 메뉴선택
                    game_framework.pop_state()
                elif(Skill_Bool == False):          # 스킬선택
                    Menu_Bool = False

            elif event.key == SDLK_a:
                pass
    pass


def update():
    pass


def draw():
    clear_canvas()
    play_state. Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)                          # 흰배경
    Poketmon.Poket_Data[wild_Poketmon.Num].Front_Draw(500,450,224,224)                      # 야생포켓몬 그리기
    Poketmon.Poket_Data[play_state.hero.pList[0].Num].Back_Draw(120, 200, 224, 224)         # 내 포켓몬 그리기
    update_canvas()
    pass