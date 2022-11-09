from pico2d import *
import Battle
import play_state
import Poketmon
import Skill_Data
from random import randint
import Battle_Choose
import game_framework
import Exp_state
import Evolution_state
import Font
from Map import Maping
import Sub_Draw

Battle_type = None
select_Poketmon,Enermy_Poketmon = None,None
select_M = None                             # 현재 커서 위치(메뉴선택과 스킬선택할 때 사용.
Menu_Bool,Skill_Bool = None,None            # 메뉴선택, 스킬선택
rand = randint
Cursor_image = None
Order_Que,Order,round,gap,Push_type,Ncount,Pcount = None,None,None,None,None,None,None
exp_bar,DrawFrame = None,None
Enermy_Down,My_Down = False,False

def enter():
    global select_Poketmon,Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Cursor_image,Order_Que,Order,exp_bar,round,Pcount,DrawFrame
    Cursor_image = load_image('./resource/image/Cursor.png')
    exp_bar = load_image('./resource/image/Exp_bar.png')
    Order_Que = []
    Order = None
    round = -1
    Pcount = 100
    if(Battle_type == 'Wild'):
        if(play_state.round == 1):
            select_Poketmon = [9,11,14,17,22,24]                    # 29번 도로에서 위 도감 번호 포켓몬 중
            Enermy_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0,len(select_Poketmon)-1)],rand(3,10),30)  # 랜덤 포켓몬 생성
            pass
        else:
            select_Poketmon = [10, 13, 16, 18,20, 23, 25]           # 31번 도로
            Enermy_Poketmon = Poketmon.Wild_Poketmon(select_Poketmon[rand(0, len(select_Poketmon) - 1)], rand(10, 20), 30)
            pass
    elif(Battle_type == 'Trainer'):
        Pcount = 0
        Enermy_Poketmon = Maping[play_state.round].Npc[Ncount].Poket[Pcount]
        select_Poketmon = 0
        print(Enermy_Poketmon.Num)
    Enermy_Poketmon.Set_ability()                                 # 야생 포켓몬 능력치 세팅
    Enermy_Poketmon.Set_Skill()                                   # 야생 포켓몬 스킬 분배
    Enermy_Poketmon.init_Change_ability()
    Battle.Poket_Order_Check()
    play_state.hero.pList[Battle.Poket_Order].init_Change_ability()
    DrawFrame = 0


    del (select_Poketmon)                                       # 필요 없어진 배열 삭제.
    select_M = 0
    Menu_Bool, Skill_Bool = False,False
    pass


def exit():
    for i in play_state.hero.pList:
        i.MinusY = 0
    if(Battle_type != 'Wild'):
        for i in Maping[play_state.round].Npc[Ncount].Poket:
            i.MinusY = 0
    global Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Order_Que,round
    del(Enermy_Poketmon)
    play_state.hero.pList[Battle.Poket_Order].del_Change_ability()
    del(select_M)
    del(Menu_Bool,Skill_Bool,Order_Que,round)
    pass


def pause():
    pass


def handle_events():
    global Menu_Bool,Skill_Bool,select_M,Order_Que,Order,round,Push_type

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
                elif (Skill_Bool == False and select_M < len(play_state.hero.pList[Battle.Poket_Order].Skill_List) - 1):
                    select_M += 1

            elif event.key == SDLK_a:
                if(Menu_Bool == False):
                    if(select_M == 0):
                        Menu_Bool = True
                        select_M = 0
                    if (select_M == 1):
                        game_framework.push_state(Battle_Choose)
                        Push_type = 'Battle_Choose'
                        select_M = 0
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
    global round,gap,Order,Push_type,select_M,DrawFrame,Enermy_Down,My_Down
    if(Order != None):
        if(Order==0):                       # 내 포켓몬 공격 체크
            if(play_state.hero.pList[Battle.Poket_Order].ailment_check()):
                gap = Enermy_Poketmon.Hp
                round  = 8

            if(round == 0):
                gap = Enermy_Poketmon.Hp
                round = play_state.hero.pList[Battle.Poket_Order].Use_Skill(Enermy_Poketmon, select_M,True)
                Hp = Enermy_Poketmon.Hp
                Enermy_Poketmon.Hp = gap
                gap = Hp
                print('attack1')
            elif (Enermy_Poketmon.Hp != gap and round > 7):
                Enermy_Poketmon.Hp -= 1
                select_M = 0
            elif (round > 7):
                Order = Order_Que.pop(0)
                round = -2
                select_M = 0


            round += 1

            if (Enermy_Poketmon.Hp <= 0):
                Enermy_Down = True
                Order = None


        elif(Order == 1):               # 상대 포켓몬 공격체크
            if (Enermy_Poketmon.ailment_check()):
                gap = play_state.hero.pList[Battle.Poket_Order].Hp
                round = 8

            if(round == 0):
                print(play_state.hero.pList[Battle.Poket_Order].Hp)
                gap = play_state.hero.pList[Battle.Poket_Order].Hp
                round = Enermy_Poketmon.Use_Skill(play_state.hero.pList[Battle.Poket_Order], 1,False)
                Hp = play_state.hero.pList[Battle.Poket_Order].Hp
                play_state.hero.pList[Battle.Poket_Order].Hp = gap
                gap = Hp
            elif(play_state.hero.pList[Battle.Poket_Order].Hp != gap and round > 7):
                print(play_state.hero.pList[Battle.Poket_Order].Hp,gap)
                play_state.hero.pList[Battle.Poket_Order].Hp -= 1
            elif(round>7):
                Order = Order_Que.pop(0)
                round = -2
                print(12121212)



            round += 1

            if (play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
                My_Down = True

    DrawFrame +=1

    if(Enermy_Down):
        Enermy_Poketmon.MinusY += 3
        if(Enermy_Poketmon.MinusY >=56):
            game_framework.push_state(Exp_state)
            Push_type = 'Exp_state'
            Enermy_Down= False
    elif(My_Down):
        play_state.hero.pList[Battle.Poket_Order].MinusY += 3
        if(play_state.hero.pList[Battle.Poket_Order].MinusY >= 56):
            game_Continue = False
            for i in play_state.hero.pList:
                print('Hp', i.Hp)
                if i.Hp != 0:
                    game_Continue = True

            if game_Continue:
                Order = None
                game_framework.push_state(Battle_Choose)
                Push_type = 'Battle_Choose'
                print(Order)
            else:
                game_framework.pop_state()
            My_Down = False
    pass


def draw():
    global DrawFrame
    clear_canvas()
    if(DrawFrame<29):
        Sub_Draw.Emergence(DrawFrame)
        delay(0.001)
    elif(DrawFrame<77 and Battle_type != 'Wild'):
        Sub_Draw.Throw_Monster(DrawFrame)
        delay(0.005)
    else:
        draw_world()
        delay(0.05)
    update_canvas()

    pass

def draw_world():
    play_state.Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)  # 흰배경

    if(not (Order == 0 and (round == 3 or round == 5 or round == 7)) ):
        Enermy_Poketmon.Front_Draw(500, 450,56,56, 224, 224)  # 야생포켓몬 그리기
    if (not (Order == 1 and (round == 3 or round == 5 or round == 7))):
        play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 200,48, 47, 224, 224)  # 내 포켓몬 그리기

    if((Menu_Bool != True or Skill_Bool != True) and Order == None):
        play_state.Board.clip_draw(0, 1, 83, 76, 440, 160, 380, 180)
        Cursor_image.clip_draw(0, 0, 32, 32, 280 + (180 * (select_M % 2)), 200 - (80 * (select_M // 2)),16,16)
        if(Menu_Bool == False):
            Font.Draw_Al('Skill', 300 , 200 , 16,16)
            Font.Draw_Al('Poketmon', 480, 200, 16, 16)
            Font.Draw_Al('Inven', 300, 120, 16, 16)
            Font.Draw_Al('Run', 480, 120, 16, 16)
        elif(Menu_Bool == True):
            for i in range(0, len(play_state.hero.pList[Battle.Poket_Order].Skill_List)):  # 포켓몬 타입 출력
                Font.Draw_Al(Skill_Data.Attack[play_state.hero.pList[Battle.Poket_Order].Skill_List[i]].name, 300 + (180 * (i % 2)), 200 - (80 * (i // 2)), 12,12)

    play_state.Font_image.clip_draw(275, 446, 8, 8, 470, 300, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 490, 300, 16, 16)  # L
    Font.Draw_Num( play_state.hero.pList[Battle.Poket_Order].level,540,300,16,16)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 490, 275, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 419, 275, 383 * (play_state.hero.pList[Battle.Poket_Order].Hp / play_state.hero.pList[Battle.Poket_Order].MaxHp), 15)
    exp_bar.clip_draw(0, 0, 2, 2, 419, 260, 383 * ( play_state.hero.pList[Battle.Poket_Order].Exp / (play_state.hero.pList[Battle.Poket_Order].level * 50)),10)

    play_state.Font_image.clip_draw(275, 446, 8, 8, 170, 550, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 190, 550, 16, 16)  # L
    Font.Draw_Num(Enermy_Poketmon.level, 240, 550, 16, 16)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 190, 520, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 118, 520, 383 * (Enermy_Poketmon.Hp / Enermy_Poketmon.MaxHp), 15)



def resume():
    global Push_type,Enermy_Poketmon,Pcount,DrawFrame

    if(Battle_type == 'Wild' or Pcount + 1 >=len(Maping[play_state.round].Npc[Ncount].Poket)):
        if (Push_type == 'Exp_state' and Poketmon.Poket_Data[play_state.hero.pList[Battle.Poket_Order].Num].Evolution <= play_state.hero.pList[Battle.Poket_Order].level):
            game_framework.push_state(Evolution_state)
        elif(Push_type == 'Exp_state'):
            game_framework.pop_state()
        elif (Push_type == 'Battle_Choose' and play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
            game_framework.pop_state()
            Push_type = None
        else:
            Push_type = None
    else:
        Pcount +=1
        Enermy_Poketmon = Maping[play_state.round].Npc[Ncount].Poket[Pcount]
        Enermy_Poketmon.Set_ability()  # 야생 포켓몬 능력치 세팅
        Enermy_Poketmon.Set_Skill()  # 야생 포켓몬 스킬 분배
        Enermy_Poketmon.init_Change_ability()
        DrawFrame = 29
    pass

def pause():
    pass
