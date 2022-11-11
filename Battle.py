from pico2d import *
import game_framework
import Poketmon
import Skill_Data
from random import randint
import play_state
import wild_Battle

Poket_Order= None
def Speed_check(My,Enermy):
    if((My.Speed * (1 + 1 / 4 * My.ChangeSp)) > (Enermy.Speed * (1 + 1 / 4 * Enermy.ChangeSp))):
        return [My,Enermy,None],[Enermy,My,None]
    else:
        return [Enermy,My,None],[My,Enermy,None]

def Poket_Order_Check():
    global Poket_Order
    Poket_Order = 0
    for i in play_state.hero.pList:
        if i.Hp != 0:
            break
        else:
            Poket_Order += 1

def Death_Check(Defenser):
    if(Defenser == wild_Battle.Enermy_Poketmon):
        return True,False

    elif(Defenser == play_state.hero.pList[Poket_Order]):
        return False,True
