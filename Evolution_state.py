from pico2d import *
import game_framework
import wild_Battle
import play_state
from Map import Maping

frame = None

def enter():
    global frame
    frame = 0
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                if(frame == 39):
                    game_framework.pop_state()
    pass

def update():
    global frame


    if(frame != 39):
        frame += 1
        if (frame % 2 == 1):
            play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num += 1
        elif(frame % 2 == 0):
            play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num -= 1
    pass

def draw():
    clear_canvas()


    Maping[19].map.clip_draw(Maping[19].Nowx, Maping[19].Nowy, 640, 576, 320, 288)

    play_state.hero.pList[wild_Battle.Battle.Poket_Order].Front_Draw(320, 288,56,56, 224, 224)  # 내 포켓몬 그리기

    if (frame >= 30 and frame < 32):
        Maping[18].map.clip_draw(Maping[18].Nowx, Maping[18].Nowy, 640, 576, 320, 288)
    elif (30<frame < 34):
        Maping[17].map.clip_draw(Maping[17].Nowx, Maping[17].Nowy, 640, 576, 320, 288)
    elif (30<frame < 36):
        Maping[16].map.clip_draw(Maping[16].Nowx, Maping[16].Nowy, 640, 576, 320, 288)
    elif (frame < 38 and frame>30):
        Maping[15].map.clip_draw(Maping[15].Nowx, Maping[15].Nowy, 640, 576, 320, 288)


    delay(0.05)

    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():

    delay(0.2)
    play_state.hero.pList[wild_Battle.Battle.Poket_Order].Set_ability()
    play_state.hero.Meet_Npc = None
    pass