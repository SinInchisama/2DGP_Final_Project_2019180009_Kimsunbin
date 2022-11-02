from pico2d import *
import play_state
import Poketmon
import Skill_Data
from random import randint

import game_framework

select_Poketmon,wild_Poketmon = None,None
select_M = None                             # 현재 커서 위치(메뉴선택과 스킬선택할 때 사용.
Menu_Bool,Skill_Bool = None,None            # 메뉴선택, 스킬선택
rand = randint
Cursor_image = None

def enter():
    global select_Poketmon,wild_Poketmon,select_M,Menu_Bool,Skill_Bool,Cursor_image
    Cursor_image = load_image('./resource/image/Cursor.png')

    if(play_state.round == 1):
        select_Poketmon = [9,11,14,17,22,24]                    # 29번 도로에서 위 도감 번호 포켓몬 중
        wild_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0,len(select_Poketmon)-1)],rand(3,10),30)  # 랜덤 포켓몬 생성
        pass
    else:
        select_Poketmon = [10, 13, 16, 18,20, 23, 25]           # 31번 도로
        wild_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0, len(select_Poketmon) - 1)], rand(10, 20), 30)
        pass
    wild_Poketmon.Set_ability()                                 # 야생 포켓몬 능력치 세팅
    wild_Poketmon.Set_Skill()                                   # 야생 포켓몬 스킬 분배
    wild_Poketmon.init_Change_ability()
    play_state.hero.pList[0].init_Change_ability()


    del (select_Poketmon)                                       # 필요 없어진 배열 삭제.
    select_M = 0
    Menu_Bool, Skill_Bool = False,False
    pass


def exit():
    global wild_Poketmon,select_M,Menu_Bool,Skill_Bool
    del(wild_Poketmon)
    play_state.hero.pList[0].del_Change_ability()
    del(select_M)
    del(Menu_Bool,Skill_Bool)
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    global Menu_Bool,Skill_Bool,select_M

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                if(Menu_Bool == False):             # 메뉴선택
                    game_framework.pop_state()
                elif(Skill_Bool == False):          # 스킬선택
                    select_M = 0
                    Menu_Bool = False

            elif event.key == SDLK_LEFT:
                if(select_M>0):
                    select_M -= 1

            elif event.key == SDLK_RIGHT:
                if (Menu_Bool == False and select_M < 3):
                    select_M += 1
                elif (Skill_Bool == True and select_M < len(play_state.hero.pList[0].Skill_List)):
                    select_M += 1

            elif event.key == SDLK_a:
                print(wild_Poketmon.Hp)
                Skill_Data.Attack[play_state.hero.pList[0].Skill_List[0]].Use(wild_Poketmon,play_state.hero.pList[0])
                print(wild_Poketmon.Hp)
                pass
            elif event.key == SDLK_b:
                print(wild_Poketmon.Hp)
                Skill_Data.Attack[play_state.hero.pList[0].Skill_List[1]].Use(wild_Poketmon,play_state.hero.pList[0])
                print(wild_Poketmon.Hp)
                pass
            elif event.key == SDLK_c:
                play_state.hero.pList[0].ChangePa += 1
    pass


def update():
    pass


def draw():
    clear_canvas()
    play_state. Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)                          # 흰배경
    Poketmon.Poket_Data[wild_Poketmon.Num].Front_Draw(500,450,224,224)                      # 야생포켓몬 그리기
    Poketmon.Poket_Data[play_state.hero.pList[0].Num].Back_Draw(120, 200, 224, 224)         # 내 포켓몬 그리기

    if(Menu_Bool != True or Skill_Bool != True):
        Cursor_image.clip_draw(0, 0, 32, 32, 330 + (150 * (select_M % 2)), 200 - (80 * (select_M // 2)))
    update_canvas()
    pass