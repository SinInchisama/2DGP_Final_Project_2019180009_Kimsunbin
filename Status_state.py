from pico2d import *
import game_framework
import play_state
import Poketmon
import Choose_Poketmon
import Font

Status_iamge = None
select = None
NowPc,Nowlv = None,None            # 현재 포켓몬카운트
RHp= None
ability = None

def enter():
    global Status_iamge,select,NowPc,Nowlv
    global RHp,ability
    Status_iamge = [load_image('./resource/image/Status_state.png')]
    Status_iamge.append(load_image('./resource/image/Skill_state.png'))
    Status_iamge.append(load_image('./resource/image/ability_state.png'))
    select = 0
    NowPc = Choose_Poketmon.CusorY
    Nowlv = play_state.hero.pList[NowPc].level
    pass

def handle_events():
    global select,ability,Nowlv
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if(select - 1 >= 0):
                    select -= 1
            elif event.key == SDLK_RIGHT:
                select = (select + 1) % 3

            elif event.key == SDLK_UP:
                play_state.hero.pList[0].Num += 1

            elif event.key == SDLK_DOWN:
                play_state.hero.pList[0].Num -= 1


            elif event.key == SDLK_a:
                play_state.hero.pList[NowPc].level += 1

            elif event.key == SDLK_s:
                play_state.hero.pList[NowPc].level -= 1

            elif event.key == SDLK_b:
                game_framework.pop_state()
                break






def update():
    pass

def draw():
    clear_canvas()
    Status_iamge[select].clip_draw(0,0,160,144,320,288,640,576)
    # Poketmon.Poket_Data.image.clip_draw(Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].Pngx, Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].Pngy, 56, 56, 120, 450, 224, 224)
    Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].Front_Draw(120,450,224,224)

    Font.Draw_Num(play_state.hero.pList[NowPc].Num + 1, 345, 555, 20, 20)  # Hp 출력


    Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].name,264,490,32,32)
    Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].name, 335, 435, 32,32)

    if select == 0:
        Select_0()
    elif select == 2:
        Select_2()
    update_canvas()
    pass

def exit():
    pass

def Select_0():
    play_state.HPbar_image.clip_draw(0,0,2,15,64,273,383 * (play_state.hero.pList[NowPc].Hp / play_state.hero.pList[NowPc].MaxHp),15)

    Font.Draw_Num(play_state.hero.pList[NowPc].Hp,110,240,32,32)        # Hp 출력

    Font.Draw_Num(play_state.hero.pList[NowPc].MaxHp, 240, 240, 32, 32) # Max Hp 출력

    Font.Draw_Num(play_state.hero.pList[NowPc].Exp, 600, 230, 32, 32)  # 현재 경험치 출력

    Font.Draw_Num(play_state.hero.pList[NowPc].level * 50-play_state.hero.pList[NowPc].Exp, 600, 115, 32, 32)  # 남은 경험치 출력





    for i in range(0,len(Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].type)):  # 포켓몬 타입 출력
        Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[NowPc].Num].type[i], 40, 70 - (32 * i), 32, 32)
        
    pass

def Select_2():
    #RHp,RPattack,  RPdefense, RSattack, RSdefense, RSpeed
    ycount = 0
    # for i in ability:
    #     Acount, div = 0, 1
    #     while i // div != 0:  # 현재 경험치 출력
    #         result = (i // div) % 10
    #         play_state.Font_image.clip_draw(221 + result * 9, 392, 8, 8, 630 - (Acount * 32), 276 - (ycount * 65), 32, 32)
    #         Acount += 1
    #         div *= 10
    #     ycount += 1
    pass