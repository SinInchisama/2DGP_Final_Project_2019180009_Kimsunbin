from pico2d import *
import game_framework
import Status_state
import play_state
import Poketmon
import Font
import wild_Battle
import Battle

Choose_image = None
Cursor_image = None
CusorY = None
frame = None
Pframe = None
Round = None
Now_Select = None

def enter():
    global Menu_image,CusorY,Cursor_image,frame,Pframe,Round,Now_Select
    Menu_image = load_image('./resource/image/Choose_Poketmon.png')
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    frame = 0
    Pframe = 0
    Round = 0

    pass

def handle_events():
    global CusorY,frame,Round,Now_Select

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                if(Round == 1):
                    CusorY = (CusorY+1) % 3
                elif(Round == 0):
                    if CusorY + 1 < play_state.hero.Pcount:
                        CusorY = (CusorY + 1) % 7
                    else:
                        CusorY = 6
                elif(Round == 2):
                    if CusorY + 1 < play_state.hero.Pcount:
                        CusorY = (CusorY + 1) % 7
                    else:
                        CusorY = play_state.hero.Pcount - 1

            elif event.key == SDLK_UP:

                if(Round == 1):
                    if(CusorY > 0):
                        CusorY -= 1
                else:
                    if(CusorY == 6):
                        CusorY = play_state.hero.Pcount -1
                    elif(CusorY >0):
                        CusorY-= 1


            elif event.key == SDLK_a:
                if(Round == 0):
                    if (CusorY != 6):
                        if(play_state.hero.inventory.Nowitem != -1):                         # 아이템 사용
                            play_state.hero.pList[CusorY].Hp = (play_state.hero.pList[CusorY].Hp +
                                                                play_state.hero.inventory.Heal[play_state.hero.inventory.Nowitem][0].Use_daily())
                            if(play_state.hero.pList[CusorY].Hp > play_state.hero.pList[CusorY].MaxHp):
                                play_state.hero.pList[CusorY].Hp = play_state.hero.pList[CusorY].MaxHp
                            if(play_state.hero.inventory.Use_type == 'Use_battle'):
                                wild_Battle.Attacker, wild_Battle.Defenser = wild_Battle.Enermy_Poketmon, play_state.hero.pList[Battle.Poket_Order]
                                wild_Battle.Order_Que1, wild_Battle.Order_Que2, wild_Battle.round = [None], [None], 0
                            play_state.hero.inventory.Heal[play_state.hero.inventory.Nowitem][1] -= 1
                            game_framework.pop_state()

                        else:
                            Round = 1
                            Now_Select = CusorY
                            CusorY = 0

                    elif (CusorY == 6):
                        game_framework.pop_state()

                elif (Round == 1):
                    if(CusorY == 0):
                        game_framework.push_state(Status_state)
                    elif(CusorY == 1):
                        if (len(play_state.hero.pList) > 1):
                            CusorY = 0
                            Round = 2
                    elif(CusorY == 2):
                        CusorY = 0
                        Round = 0

                elif(Round == 2):
                    if(CusorY != 6 and CusorY != Now_Select):
                        Change_Poke(CusorY,Now_Select)
                        Round = 0
            elif event.key == SDLK_ESCAPE:
                if(Round==0):
                    game_framework.pop_state()
                elif(Round == 1):
                    Round = 0
                    CusorY = 0



def draw():
    clear_canvas()
    Menu_image.clip_draw(5 + frame, 7, 640, 576, 320, 288)

    for i in range(0,play_state.hero.Pcount):           # player가 가진 포켓몬 숫자만큼 출력
        play_state.hero.character_image.clip_draw(220 + (int(Pframe) * 34),610,36,36,45,525- (64 * i))      # 포켓몬 이미지

        Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[i].Num].name,80,520 - (64 * i),16,16)        # 포켓몬 이름

        play_state.Font_image.clip_draw(275, 446, 8, 8, 260, 520 - (64 * i), 16, 16)        # :
        play_state.Font_image.clip_draw(266, 455, 8, 8, 280, 520 - (64 * i), 16, 16)        # L

        Font.Draw_Num(play_state.hero.pList[i].level,340,520-(64*i),16,16)          # 레벨

        Font.Draw_Num(play_state.hero.pList[i].Hp, 470, 540 - (64 * i), 16, 16)     # 체력

        Font.Draw_Num(play_state.hero.pList[i].MaxHp, 550, 540 - (64 * i), 16, 16)


        play_state.Hp_image.clip_draw(0,0,68,6,490,520 - (64 * i),272,20)

        play_state.HPbar_image.clip_draw(0, 0, 2, 15, 419, 520 - (64 * i), 383 * (play_state.hero.pList[i].Hp / play_state.hero.pList[i].MaxHp),15)

        play_state.Font_image.clip_draw(194, 392, 8, 8, 500, 540 - (64 * i), 16, 16)

    if(Round == 1):
        play_state.Board.clip_draw(0, 1, 83, 76, 516, 75, 249, 180)
        Font.Draw_Al('View Status', 440, 130, 16, 16)
        Font.Draw_Al('Change Poke', 440, 80, 16, 16)
        Font.Draw_Al('Close Menu', 440, 30, 16, 16)

    if(Round == 0 or Round == 2):
        Cursor_image.clip_draw(0, 0, 32, 32, 15, 525 - (64 * CusorY))           # 커서 위치
    elif(Round == 1):
        Cursor_image.clip_draw(0, 0, 32, 32, 420, 130 - (50 * CusorY),16,16)  # 커서 위치

    update_canvas()
    pass

def update():
    global Pframe
    Pframe = (Pframe + 0.01) % 2
    pass

def exit():
    play_state.hero.inventory.Nowitem = -1
    play_state.hero.inventory.Use_type = ''
    pass

def pause():
    pass

def resume():
    global CusorY
    CusorY = 0
    pass


def Change_Poke(Num1,Num2):     # 포켓몬 위치교환을 하는 함수
    Save_Poke = play_state.hero.pList[Num1]
    play_state.hero.pList[Num1] = play_state.hero.pList[Num2]
    play_state.hero.pList[Num2] = Save_Poke