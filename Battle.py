from pico2d import *
import game_framework
import Poketmon
import Skill_Data
from random import randint
import play_state

Poket_Order= None
def Speed_check(My,Enermy):
    if((My.Speed * (1 + 1 / 4 * My.ChangeSp)) > (Enermy.Speed * (1 + 1 / 4 * Enermy.ChangeSp))):
        return [0,1,None]
    else:
        return [1,0,None]

def Poket_Order_Check():
    global Poket_Order
    Poket_Order = 0
    for i in play_state.hero.pList:
        if i.Hp != 0:
            break
        else:
            Poket_Order += 1