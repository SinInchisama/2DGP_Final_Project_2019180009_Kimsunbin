from pico2d import *
import game_framework

import Poketmon
import Skill_Data
from random import randint

def Speed_check(My,Enermy):
    if(My.Speed * (1 + 1 / 4 * Enermy.ChangeSp) > My.Speed * (1 + 1 / 4 * Enermy.ChangeSp)):
        return [1,0]
    else:
        return [0,1]