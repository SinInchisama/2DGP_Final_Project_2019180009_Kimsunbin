from pico2d import *
import game_framework
import Poketmon
import Skill_Data
from random import randint

def Speed_check(My,Enermy):
    if((My.Speed * (1 + 1 / 4 * My.ChangeSp)) > (Enermy.Speed * (1 + 1 / 4 * Enermy.ChangeSp))):
        return [0,1,None]
    else:
        return [1,0,None]