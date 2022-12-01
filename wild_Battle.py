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
import View_inventory
import Heal_state


Battle_type = None
select_Poketmon,Enermy_Poketmon = None,None
select_M = None                             # 현재 커서 위치(메뉴선택과 스킬선택할 때 사용.
Menu_Bool,Skill_Bool = None,None            # 메뉴선택, 스킬선택
rand = randint
Cursor_image = None
Order_Que1,Order_Que2,Attacker,Defenser,round,gap,Push_type,Pcount = None,None,None,None,None,None,None,None
exp_bar,DrawFrame,round1 = None,None,None
Enermy_Down,My_Down,Now_Pcount ,Attacker_type= False,False,None,None

def enter():
    global select_Poketmon,Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Cursor_image,Order_Que1,Order_Que2,Attacker,Defenser,exp_bar,round,Pcount,DrawFrame,Now_Pcount,Attacker_type,round1
    round1 = play_state.round
    play_state.Battle_Music.repeat_play()
    Cursor_image = load_image('./resource/image/Cursor.png')
    exp_bar = load_image('./resource/image/Exp_bar.png')
    Order_Que1,Order_Que2 = [],[]
    Attacker,Defenser = None,None
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
        Enermy_Poketmon = Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Poket[Pcount]
        select_Poketmon = 0
    Enermy_Poketmon.Set_ability()                                 # 야생 포켓몬 능력치 세팅
    Enermy_Poketmon.Set_Skill()                                   # 야생 포켓몬 스킬 분배
    Enermy_Poketmon.init_Change_ability()
    Battle.Poket_Order_Check()
    play_state.hero.pList[Battle.Poket_Order].init_Change_ability()
    play_state.Pokedex.PokeDex_View_check(Enermy_Poketmon.Num)
    DrawFrame = 0
    Now_Pcount = play_state.hero.Pcount


    del (select_Poketmon)                                       # 필요 없어진 배열 삭제.
    select_M = 0
    Menu_Bool, Skill_Bool = False,False
    Attacker_type = ' '
    pass


def exit():
    global Push_type
    for i in play_state.hero.pList:
        i.MinusY = 0
    if(Battle_type != 'Wild'):
        for i in Maping[round1].Npc[play_state.hero.Meet_Npc].Poket:
            i.MinusY = 0
    global Enermy_Poketmon,select_M,Menu_Bool,Skill_Bool,Order_Que1,Order_Que2,round
    del(Enermy_Poketmon)
    play_state.hero.pList[Battle.Poket_Order].del_Change_ability()
    del(select_M)
    del(Menu_Bool,Skill_Bool,Order_Que1,Order_Que2,round)
    Push_type = None
    play_state.Back_Music.repeat_play()
    pass


def pause():
    pass


def handle_events():
    global Menu_Bool,Skill_Bool,select_M,Order_Que1,Order_Que2,Attacker,Defenser,round,Push_type,Attacker_type,gap

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
                    elif (select_M == 1):
                        game_framework.push_state(Battle_Choose)
                        Push_type = 'Battle_Choose'
                        select_M = 0
                    elif(select_M == 2):
                        play_state.hero.inventory.Use_type = 'Use_battle'
                        Push_type = 'View_inventory'
                        game_framework.push_state(View_inventory)
                            # game_framework.push_state(Throw_Ball)
                            # Push_type = 'Throw_Ball'
                    elif(select_M == 3):
                        game_framework.pop_state()
                    pass
                elif (Skill_Bool == False):
                    Menu_Bool = False
                    Order_Que1,Order_Que2 = Battle.Speed_check(play_state.hero.pList[Battle.Poket_Order],Enermy_Poketmon)
                    Attacker,Defenser = Order_Que1.pop(0),Order_Que2.pop(0)
                    if (Attacker.ailment_check()):
                        gap = Defenser.Hp
                        Attacker_type = Attacker.ailment
                    round = 0
                    pass



def update():
    global round,gap,Push_type,select_M,DrawFrame,Enermy_Down,My_Down,Attacker,Defenser,Order_Que1,Order_Que2,Attacker_type
    if(Attacker != None):
        if(round == 0):
            if(Attacker_type == ' '):
                gap = Defenser.Hp
                if(Attacker == Enermy_Poketmon):
                    Enermy_Poketmon.What_Use_Skill()
                    Attacker_type = Attacker.Check_Use(Enermy_Poketmon.Use)
                    if (Attacker_type == 'Use'):
                        Attacker.Use_Skill(Defenser, Enermy_Poketmon.Use)
                else:
                    Attacker_type = Attacker.Check_Use(select_M)
                    if (Attacker_type == 'Use'):
                        Attacker.Use_Skill(Defenser, select_M)
                Hp = Defenser.Hp
                Defenser.Hp = gap
                gap = Hp
        elif (Defenser.Hp != gap and round > 13):
            Defenser.Hp -= 1

            if (Defenser.Hp <= 0):
                Enermy_Down, My_Down=Battle.Death_Check(Defenser)
                Attacker,Defenser,Order_Que1,Order_Que2 = None,None,[],[]

        elif (round > 20):
            if (Attacker != Enermy_Poketmon):  # 내 포켓몬이 공격했으면 select_M을 초기화
                select_M = 0
            Attacker = Order_Que1.pop(0)
            Defenser = Order_Que2.pop(0)
            Attacker_type = ' '
            if(Attacker != None):
                if (Attacker.ailment_check()):
                    gap = Defenser.Hp
                    Attacker_type = Attacker.ailment
            round = -1
        round += 1

    DrawFrame +=1

    if(Enermy_Down):
        Enermy_Poketmon.MinusY += 3
        if(Enermy_Poketmon.MinusY >=56):
            game_framework.push_state(Exp_state)
            Push_type = 'Exp_state'

    elif(My_Down):
        play_state.hero.pList[Battle.Poket_Order].MinusY += 3
        if(play_state.hero.pList[Battle.Poket_Order].MinusY >= 56):
            game_Continue = False
            for i in play_state.hero.pList:
                if i.Hp != 0:
                    game_Continue = True

            if game_Continue:
                Attacker = None
                game_framework.push_state(Battle_Choose)
                Push_type = 'Battle_Choose'
            else:
                if(play_state.round == 1):
                    Maping[1].Nowx,Maping[1].Nowy = 1280,0
                    play_state.round = 7
                    play_state.hero.mapx,play_state.hero.mapy,play_state.hero.chx,play_state.hero.chy =48,432,48,432
                elif(play_state.round == 3):
                    Maping[2].Nowx,Maping[2].Nowy = 192, 0
                    Maping[3].Nowx, Maping[3].Nowy = 448,0
                    play_state.round = 13
                    play_state.hero.mapx, play_state.hero.mapy, play_state.hero.chx, play_state.hero.chy = 80, 400, 80, 400
                elif(play_state.round == 22 or play_state.round == 23):
                    Maping[4].Nowx, Maping[4].Nowy = 640,0
                    play_state.round = 20
                    play_state.hero.mapx, play_state.hero.mapy, play_state.hero.chx, play_state.hero.chy = 80, 400, 80, 400
                play_state.hero.pngx = 18 + 68 + 34
                game_framework.change_state(Heal_state)
            My_Down = False

    pass


def draw():
    global DrawFrame
    clear_canvas()
    if(DrawFrame<29):
        Sub_Draw.Emergence(DrawFrame)
        delay(0.005)
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

    if(Attacker_type == ' '):
        Enermy_Poketmon.Front_Draw(500, 450, 56, 56, 224, 224)  # 야생포켓몬 그리기
        play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240, 48, 47, 224, 224)  # 내 포켓몬 그리기
    elif(Attacker_type == 'Use'):
        if(not (Defenser == Enermy_Poketmon and (round == 3 or round == 5 or round == 7)) ):
            Enermy_Poketmon.Front_Draw(500, 450,56,56, 224, 224)  # 야생포켓몬 그리기
        if (not (Defenser == play_state.hero.pList[Battle.Poket_Order] and (round == 3 or round == 5 or round == 7))):
            play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240,48, 47, 224, 224)  # 내 포켓몬 그리기
    elif(Attacker_type == 'miss'):
        Enermy_Poketmon.Front_Draw(500, 450, 56, 56, 224, 224)  # 야생포켓몬 그리기
        play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240, 48, 47, 224, 224)  # 내 포켓몬 그리기
    elif (Attacker_type == 'Paralysis'):
        if(round < 30):
            if(Attacker == Enermy_Poketmon):
                Enermy_Poketmon.Front_Draw(500, 447 + (round % 2) * 6, 56, 56, 224, 224)  # 야생포켓몬 그리기
                play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240, 48, 47, 224, 224)  # 내 포켓몬 그리기
            else:
                Enermy_Poketmon.Front_Draw(500, 450, 56, 56, 224, 224)  # 야생포켓몬 그리기
                play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 237 + (round % 2) * 6, 48, 47, 224, 224)  # 내 포켓몬 그리기



    play_state.Board.clip_draw(0, 1, 83, 76, 320, 75, 644, 140)

    if(Enermy_Down != True and My_Down != True):
        if((Menu_Bool != True or Skill_Bool != True) and Attacker == None):
            play_state.Board.clip_draw(0, 1, 83, 76, 440, 100, 380, 180)
            Cursor_image.clip_draw(0, 0, 32, 32, 280 + (180 * (select_M % 2)), 140 - (80 * (select_M // 2)),16,16)
            if(Menu_Bool == False):
                Font.Draw_Al('Skill', 300, 140, 16, 16)
                Font.Draw_Al('Poketmon', 480, 140, 16, 16)
                Font.Draw_Al('Inven', 300, 60, 16, 16)
                Font.Draw_Al('Run', 480, 60, 16, 16)
            elif(Menu_Bool == True):
                for i in range(0, len(play_state.hero.pList[Battle.Poket_Order].Skill_List)):  # 포켓몬 타입 출력
                    Font.Draw_Al(Skill_Data.Attack[play_state.hero.pList[Battle.Poket_Order].Skill_List[i]].name,
                                 300 + (180 * (i % 2)), 140 - (80 * (i // 2)), 12, 12)
        else:
            if (Attacker_type == 'Use'):
                if(Attacker == Enermy_Poketmon):
                    Font.Draw_Al(Poketmon.Poket_Data[Attacker.Num].name + ' Use ' + Skill_Data.Attack[Attacker.Skill_List[Enermy_Poketmon.Use]].name,60, 100, 20, 20)
                else:
                    Font.Draw_Al(Poketmon.Poket_Data[Attacker.Num].name + ' Use ' + Skill_Data.Attack[
                        Attacker.Skill_List[select_M]].name, 60, 100, 20, 20)
            elif (Attacker_type == 'miss'):
                Font.Draw_Al(Poketmon.Poket_Data[Attacker.Num].name + ' Miss Skill', 60, 100, 20, 20)
            elif (Attacker_type == 'Paralysis'):
                Font.Draw_Al(Poketmon.Poket_Data[Attacker.Num].name + ' is Paralysis', 60, 100, 20, 20)

    play_state.Font_image.clip_draw(275, 446, 8, 8, 430, 260, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 450, 260, 16, 16)  # L
    if(play_state.hero.pList[Battle.Poket_Order].ailment != None):
        Font.Draw_Al(play_state.hero.pList[Battle.Poket_Order].ailment, 520, 256, 8, 8)
    Font.Draw_Num( play_state.hero.pList[Battle.Poket_Order].level,500,260,16,16)
    Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[Battle.Poket_Order].Num].name, 360,290, 24, 24)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 450, 230, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 379, 230, 383 * (play_state.hero.pList[Battle.Poket_Order].Hp / play_state.hero.pList[Battle.Poket_Order].MaxHp), 15)
    exp_bar.clip_draw(0, 0, 2, 2, 379, 215, 383 * ( play_state.hero.pList[Battle.Poket_Order].Exp / (play_state.hero.pList[Battle.Poket_Order].level * 50)),10)

    Font.Draw_Al(Poketmon.Poket_Data[Enermy_Poketmon.Num].name, 100, 540, 24, 24)
    play_state.Font_image.clip_draw(275, 446, 8, 8, 170, 510, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 190, 510, 16, 16)  # L
    Font.Draw_Num(Enermy_Poketmon.level, 240, 510, 16, 16)
    if (Enermy_Poketmon.ailment != None):
        Font.Draw_Al(Enermy_Poketmon.ailment, 260, 510, 8, 8)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 190, 480, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 118, 480, 383 * (Enermy_Poketmon.Hp / Enermy_Poketmon.MaxHp), 15)



def resume():
    global Push_type,Enermy_Poketmon,Pcount,DrawFrame,Enermy_Down,My_Down,round,Attacker_type

    # if(Battle_type == 'Wild' or Pcount + 1 >=len(Maping[play_state.round].Npc[Ncount].Poket)):
    #     elif (Push_type == 'Battle_Choose' and play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
    #         game_framework.pop_state()
    #         Push_type = None
    #     else:
    #         Push_type = None
    if(Push_type == 'Exp_state'):
        if(Battle_type != 'Wild' and Pcount + 1 < len(Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Poket)):
            Pcount += 1
            Enermy_Poketmon = Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Poket[Pcount]
            Enermy_Poketmon.Set_ability()  # 야생 포켓몬 능력치 세팅
            Enermy_Poketmon.Set_Skill()  # 야생 포켓몬 스킬 분배
            Enermy_Poketmon.init_Change_ability()
            DrawFrame = 29
            play_state.Pokedex.PokeDex_View_check(Enermy_Poketmon.Num)
            Attacker_type = ' '
            round = 0
        else:
            if(Battle_type != 'Wild'):
                Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Met = True
            if (Push_type == 'Exp_state' and Poketmon.Poket_Data[play_state.hero.pList[Battle.Poket_Order].Num].Evolution <=
                    play_state.hero.pList[Battle.Poket_Order].level):
                game_framework.change_state(Evolution_state)
            else:
                game_framework.pop_state()
                play_state.hero.Meet_Npc = None
            play_state.hero.Gold += 100
        Enermy_Down = False
    elif(Push_type == 'Battle_Choose'):
        if(play_state.hero.pList[Battle.Poket_Order].Hp <= 0):
            game_framework.pop_state()
            Push_type = None
            My_Down = False
        else:
            My_Down = False
            Push_type = None
        Attacker_type = ' '
        round = 0

    elif(Push_type == 'Throw_Ball'):
        if(Now_Pcount!=play_state.hero.Pcount):
            game_framework.pop_state()
            play_state.hero.Meet_Npc = None
        else:
            Push_type = None
    elif(Push_type == 'View_inventory'):
        Push_type = None


def pause():
    pass
