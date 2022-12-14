from pico2d import *
import game_framework
import wild_Battle
import play_state
import Poketmon
import Change_Skill

Plus_exp = None
Now_exp = None

def enter():
    global Plus_exp,Now_exp
    Plus_exp = wild_Battle.Enermy_Poketmon.level * 40
    Now_exp = 0
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def update():
    global Plus_exp,Now_exp

    Now_exp += 1
    play_state.hero.pList[wild_Battle.Battle.Poket_Order].Exp += 1

    if(play_state.hero.pList[wild_Battle.Battle.Poket_Order].Exp == play_state.hero.pList[wild_Battle.Battle.Poket_Order].level * 50 ):
        play_state.hero.pList[wild_Battle.Battle.Poket_Order].level += 1
        play_state.hero.pList[wild_Battle.Battle.Poket_Order].Exp = 0

        if(Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill.get(play_state.hero.pList[wild_Battle.Battle.Poket_Order].level)):
            if(len(play_state.hero.pList[wild_Battle.Battle.Poket_Order].Skill_List)<4):
                play_state.hero.pList[wild_Battle.Battle.Poket_Order].Skill_List.append(Poketmon.Poket_Data[play_state.hero.pList[wild_Battle.Battle.Poket_Order].Num].Skill[play_state.hero.pList[wild_Battle.Battle.Poket_Order].level])

            else:
                game_framework.push_state(Change_Skill)

    if(Plus_exp == Now_exp):
        game_framework.pop_state()
    pass

def draw():
    clear_canvas()

    wild_Battle.draw_world()

    delay(0.01)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    delay(0.05)
    play_state.hero.pList[wild_Battle.Battle.Poket_Order].Set_ability()
    pass