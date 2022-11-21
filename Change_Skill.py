from pico2d import *

import game_framework
import play_state
import wild_Battle
import Battle
from Map import Maping
import Poketmon
import Skill_Data
import Font

Cursory = None
def enter():
    global Cursory
    Cursory = 0
    pass

def handle_events():
    global Cursory
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                if(Cursory != 4):
                    Cursory += 1
                pass
            elif event.key == SDLK_UP:
                if(Cursory != 0):
                    Cursory -= 1
                pass
            elif event.key == SDLK_a:
                play_state.hero.pList[Battle.Poket_Order].Change_Skill(Cursory)
                game_framework.pop_state()

                pass
    pass

def update():

    pass

def draw():
    clear_canvas()
    Maping[19].map.clip_draw(Maping[19].Nowx, Maping[19].Nowy, 640, 576, 320, 288)

    count = 0
    for i in play_state.hero.pList[Battle.Poket_Order].Skill_List:
        Font.Draw_Al(Skill_Data.Attack[i].name,350,500 - (count * 90),16,16)
        count += 1

    wild_Battle.Cursor_image.clip_draw(0, 0, 32, 32, 320, 500 - (Cursory * 90),16,16)

    play_state.Board.clip_draw(0,1,83,76,170,470,249,152)

    Font.Draw_Al('Damage ', 80, 520, 16, 16)
    Font.Draw_Num(Skill_Data.Attack[play_state.hero.pList[Battle.Poket_Order].Skill_List[Cursory]].Damage, 240, 510, 16, 16)
    Font.Draw_Al('Daccur ', 80, 480, 16, 16)
    Font.Draw_Num(Skill_Data.Attack[play_state.hero.pList[Battle.Poket_Order].Skill_List[Cursory]].Daccur, 240, 470, 16,16)
    Font.Draw_Al('type ' + Skill_Data.Attack[play_state.hero.pList[Battle.Poket_Order].Skill_List[Cursory]].type, 80, 440, 16, 16)


    play_state.Board.clip_draw(0, 1, 83, 76, 170, 280, 249, 228)
    Font.Draw_Al(Skill_Data.Attack[Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill[play_state.hero.pList[wild_Battle.Battle.Poket_Order].level]].name
                 , 80, 350, 32, 32)

    Font.Draw_Al('Damage ', 80, 310, 16, 16)
    Font.Draw_Num(Skill_Data.Attack[Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill[play_state.hero.pList[wild_Battle.Battle.Poket_Order].level]].Damage
                 , 240, 300, 16, 16)

    Font.Draw_Al('Daccur ', 80, 270, 16, 16)
    Font.Draw_Num(Skill_Data.Attack[Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill[
                          play_state.hero.pList[wild_Battle.Battle.Poket_Order].level]].Daccur
                  , 240, 260, 16, 16)

    Font.Draw_Al('type ' + Skill_Data.Attack[Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill[
                          play_state.hero.pList[wild_Battle.Battle.Poket_Order].level]].type, 80, 220, 16, 16)

    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    pass