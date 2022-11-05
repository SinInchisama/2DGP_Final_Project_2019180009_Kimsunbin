from pico2d import *

import Battle
import play_state
import Poketmon
import Skill_Data
from random import randint
import Battle_Choose
import game_framework

Battle_type = None
select_Poketmon,Enermy_Poketmon = None,None
select_M = None                             # 현재 커서 위치(메뉴선택과 스킬선택할 때 사용.
Menu_Bool,Skill_Bool = None,None            # 메뉴선택, 스킬선택
rand = randint
Cursor_image = None
Order_Que,Order,round,gap = None,None,None,None
exp_bar = None

def enter():
    global select_Poketmon,Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Cursor_image,Order_Que,Order,exp_bar,round
    Cursor_image = load_image('./resource/image/Cursor.png')
    exp_bar = load_image('./resource/image/Exp_bar.png')
    Order_Que = []
    Order = None
    round = -1
    if(Battle_type == 'Wild'):
        if(play_state.round == 1):
            select_Poketmon = [9,11,14,17,22,24]                    # 29번 도로에서 위 도감 번호 포켓몬 중
            Enermy_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0,len(select_Poketmon)-1)],rand(3,10),30)  # 랜덤 포켓몬 생성
            pass
        else:
            select_Poketmon = [10, 13, 16, 18,20, 23, 25]           # 31번 도로
            Enermy_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0, len(select_Poketmon) - 1)], rand(10, 20), 30)
            pass
    Enermy_Poketmon.Set_ability()                                 # 야생 포켓몬 능력치 세팅
    Enermy_Poketmon.Set_Skill()                                   # 야생 포켓몬 스킬 분배
    Enermy_Poketmon.init_Change_ability()
    Battle.Poket_Order_Check()
    play_state.hero.pList[Battle.Poket_Order].init_Change_ability()


    del (select_Poketmon)                                       # 필요 없어진 배열 삭제.
    select_M = 0
    Menu_Bool, Skill_Bool = False,False
    pass


def exit():
    global Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Order_Que,round
    del(Enermy_Poketmon)
    play_state.hero.pList[Battle.Poket_Order].del_Change_ability()
    del(select_M)
    del(Menu_Bool,Skill_Bool,Order_Que,round)
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    global Menu_Bool,Skill_Bool,select_M,Order_Que,Order,round

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
                elif (Skill_Bool == False and select_M < len(play_state.hero.pList[Battle.Poket_Order].Skill_List)):
                    select_M += 1

            elif event.key == SDLK_a:
                if(Menu_Bool == False):
                    if(select_M == 0):
                        Menu_Bool = True
                        select_M = 0
                    if (select_M == 1):
                        game_framework.push_state(Battle_Choose)
                    if(select_M == 3):
                        game_framework.pop_state()
                    pass
                elif (Skill_Bool == False):
                    Menu_Bool = False
                    Order_Que = Battle.Speed_check(play_state.hero.pList[Battle.Poket_Order],Enermy_Poketmon)
                    Order = Order_Que.pop(0)
                    round = 0
                    pass


def update():
    global round,gap,Order
    if(Order != None):
        if(Order==0):
            if(play_state.hero.pList[Battle.Poket_Order].ailment_check()):
                round  = 8

            if(round == 0):
                gap = Enermy_Poketmon.Hp
                play_state.hero.pList[Battle.Poket_Order].Use_Skill(Enermy_Poketmon, select_M)
                Hp = Enermy_Poketmon.Hp
                Enermy_Poketmon.Hp = gap
                gap = Hp
                print('attack1')
            elif (Enermy_Poketmon.Hp != gap and round > 7):
                Enermy_Poketmon.Hp -= 1
            elif (round > 7):
                Order = Order_Que.pop(0)
                round = -1

            round += 1

            if (Enermy_Poketmon.Hp <= 0):
                game_framework.pop_state()


        elif(Order == 1):
            if (Enermy_Poketmon.ailment_check()):
                round = 8

            if(round == 0):
                gap = play_state.hero.pList[Battle.Poket_Order].Hp
                Enermy_Poketmon.Use_Skill(play_state.hero.pList[Battle.Poket_Order], 1)
                Hp = play_state.hero.pList[Battle.Poket_Order].Hp
                play_state.hero.pList[Battle.Poket_Order].Hp = gap
                gap = Hp
            elif(play_state.hero.pList[Battle.Poket_Order].Hp != gap and round > 7):
                play_state.hero.pList[Battle.Poket_Order].Hp -= 1
            elif(round>7):
                Order = Order_Que.pop(0)
                round = -1

            round += 1

            if (play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
                game_Continue = False
                for i in play_state.hero.pList:
                    print('Hp',i.Hp)
                    if i.Hp != 0:
                        game_Continue  = True

                if game_Continue :
                    Order = None
                    game_framework.push_state(Battle_Choose)
                    print(Order)
                else:
                    game_framework.pop_state()

    pass


def draw():
    clear_canvas()

    draw_world()

    delay(0.05)
    update_canvas()
    pass

def draw_world():
    play_state.Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)  # 흰배경

    if(not (Order == 0 and (round == 3 or round == 5 or round == 7)) ):
        Poketmon.Poket_Data[Enermy_Poketmon.Num].Front_Draw(500, 450, 224, 224)  # 야생포켓몬 그리기
    if (not (Order == 1 and (round == 3 or round == 5 or round == 7))):
        Poketmon.Poket_Data[play_state.hero.pList[Battle.Poket_Order].Num].Back_Draw(120, 200, 224, 224)  # 내 포켓몬 그리기

    if(Menu_Bool != True or Skill_Bool != True):
        Cursor_image.clip_draw(0, 0, 32, 32, 330 + (150 * (select_M % 2)), 200 - (80 * (select_M // 2)))

    play_state.Hp_image.clip_draw(0, 0, 68, 6, 490, 300, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 419, 300, 383 * (
                play_state.hero.pList[Battle.Poket_Order].Hp / play_state.hero.pList[Battle.Poket_Order].MaxHp), 15)

    play_state.Hp_image.clip_draw(0, 0, 68, 6, 190, 520, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 118, 520, 383 * (Enermy_Poketmon.Hp / Enermy_Poketmon.MaxHp), 15)
    exp_bar.clip_draw(0, 0, 2, 2, 419, 285, 383 *  (play_state.hero.pList[Battle.Poket_Order].Exp / (play_state.hero.pList[Battle.Poket_Order].level * 50)), 10)


def resume():
    if (play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
        game_framework.pop_state()
    pass

def pause():
    pass
