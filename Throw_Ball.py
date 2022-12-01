from pico2d import *
import Font
import game_framework
import play_state
import Poketmon
import Battle
import wild_Battle

Ball,frame,CatchCount= None,None,None

def enter():
    global Ball,frame,CatchCount
    Ball = load_image('./resource/image/Ball.png')
    frame, CatchCount = 0,0
    pass

def update():
    global  CatchCount,frame
    frame+= 1
    if(CatchCount == 0):
        if(frame == 90):
            CatchCount += 1
            frame = 0
    else:
        if(frame == 9):
            if(play_state.hero.inventory.Ball[play_state.hero.inventory.Nowitem][0].Use_battle()):
                CatchCount += 1
                frame = 1
                if(CatchCount == 4):
                    game_framework.pop_state()
            else:
                game_framework.pop_state()
    pass

def draw():
    clear_canvas()
    play_state.Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)  # 흰배경
    # if(i<40):
    #     Ball.clip_composite_draw(0,0,16,16,(i-40)*15,'',500,450+(4*(i-40)),32,32)
    # else:
    #     Ball.clip_composite_draw(0, 0, 16, 16, (i - 40) * 15, '', 500, 490 - (3 * (i - 40)), 32, 32)
    play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240, 48, 47, 224, 224)  # 내 포켓몬 그리기

    play_state.Board.clip_draw(0, 1, 83, 76, 320, 75, 644, 140)
    play_state.Font_image.clip_draw(275, 446, 8, 8, 430, 260, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 450, 260, 16, 16)  # L
    Font.Draw_Num(play_state.hero.pList[Battle.Poket_Order].level, 500, 260, 16, 16)
    Font.Draw_Al(Poketmon.Poket_Data[play_state.hero.pList[Battle.Poket_Order].Num].name, 360, 290, 24, 24)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 450, 230, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 379, 230, 383 * (
                play_state.hero.pList[Battle.Poket_Order].Hp / play_state.hero.pList[Battle.Poket_Order].MaxHp), 15)
    wild_Battle.exp_bar.clip_draw(0, 0, 2, 2, 379, 215, 383 * (
                play_state.hero.pList[Battle.Poket_Order].Exp / (play_state.hero.pList[Battle.Poket_Order].level * 50)),
                      10)

    Font.Draw_Al(Poketmon.Poket_Data[wild_Battle.Enermy_Poketmon.Num].name, 100, 540, 24, 24)
    play_state.Font_image.clip_draw(275, 446, 8, 8, 170, 510, 16, 16)  # :
    play_state.Font_image.clip_draw(266, 455, 8, 8, 190, 510, 16, 16)  # L
    Font.Draw_Num(wild_Battle.Enermy_Poketmon.level, 240, 510, 16, 16)
    play_state.Hp_image.clip_draw(0, 0, 68, 6, 190, 480, 272, 20)
    play_state.HPbar_image.clip_draw(0, 0, 2, 15, 118, 480, 383 * (wild_Battle.Enermy_Poketmon.Hp / wild_Battle.Enermy_Poketmon.MaxHp), 15)

    if (CatchCount == 0):
        wild_Battle.Enermy_Poketmon.Front_Draw(500, 450, 56, 56, 224, 224)
        Ball.clip_draw(16 * play_state.hero.inventory.Nowitem, 0, 16, 16, 240 + frame * 3, 300 + frame * 1, 32, 32)
        delay(0.005)
        pass
    else:
        if (frame < 4):
             Ball.clip_composite_draw(16 * play_state.hero.inventory.Nowitem, 0, 16, 16, 3.141592 / (1+ 0.2*frame), 'hv', 500, 400, 32, 32)
        else:
            Ball.clip_composite_draw(16 * play_state.hero.inventory.Nowitem, 0, 16, 16, 3.141592 / (1.8 + 0.2 * (4-frame)), 'hv', 500, 400, 32, 32)
            delay(0.1)

        pass
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def handle_events():
    event = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def exit():
    if(CatchCount == 4):
        play_state.hero.pList.append(Poketmon.Change_to_Wild_from_TR(wild_Battle.Enermy_Poketmon))
        play_state.hero.Pcount += 1
        if( play_state.Pokedex.list[play_state.hero.pList[play_state.hero.Pcount - 1].Num] != 2):
            play_state.Pokedex.list[play_state.hero.pList[play_state.hero.Pcount - 1].Num] = 2
            play_state.Pokedex.Catch += 1
    else:
        wild_Battle.Attacker, wild_Battle.Defenser = wild_Battle.Enermy_Poketmon, play_state.hero.pList[Battle.Poket_Order]
        wild_Battle.Order_Que1, wild_Battle.Order_Que2, wild_Battle.round = [None], [None], 0

    play_state.hero.inventory.Use_type = ''
    play_state.hero.inventory.Nowitem = -1
    pass
