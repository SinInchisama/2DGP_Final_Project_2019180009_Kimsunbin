import random

class inventory:            # 플레이어 인벤토리
    def __init__(self):
        self.Ball = []
        self.Heal = []
        self.Skill_machine = []
        self.Riding = False

class item:                 # 아이템 기본 클래스
    def __init__(self,type):
        self.type = type



class ball(item):           # 몬스터볼 기본 클래스
    def __init__(self,type,daccur):
        item.__init__(type)
        self.daccur = daccur

    def Use_battle(self):
        if(random.randint(0,100)<self.daccur):
            return True
        else:
            return False

    def Use_daily(self):
        pass


                                        # 회복약
class heal(item):                       # 피 채워지는 애니메이션을 위해 Heal 리턴하고 애니메이션 출력예정.
    def __init__(self,type,Heal):
        self.type = type
        self.Heal = Heal

    def Use_battle(self):
        return self.Heal

    def Use_daily(self):
        return self.Heal


class skill_machine(item):
    def __init__(self,type,Skill_Num):
        item.__init__(type)
        self.Skill_Num = Skill_Num
        self.Can_P = []

    def Use_battle(self):
        pass

    def Use_daily(self):
        return self.Heal
