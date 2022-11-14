import random

class inventory:            # 플레이어 인벤토리
    def __init__(self):
        self.Ball = []
        self.Heal = []
        self.Skill_machine = []
        self.Riding = False

class item:                 # 아이템 기본 클래스
    def __init__(self,type,Sell):
        self.type = type
        self.Sell = Sell



class ball(item):           # 몬스터볼 기본 클래스
    def __init__(self,type,daccur,Sell):
        item.__init__(type,Sell)
        self.daccur = daccur

    def Use_battle(self):
        if(random.randint(0,100)<self.daccur):
            return True
        else:
            return False

    def Use_daily(self):
        pass

class Monster_Ball(ball):               # 몬스터볼
    def __init__(self):
        ball.__init__('Ball',50,100)

class Super_Ball(ball):                 # 슈퍼볼
    def __init__(self):
        ball.__init__('Ball',70,200)

class Hiper_Ball(ball):                 # 하이퍼볼
    def __init__(self):
        ball.__init__('Ball',80,300)

class Master_Ball(ball):  # 마스터볼
    def __init__(self):
        ball.__init__('Ball', 100, 10000)

                                        # 회복약
class heal(item):                       # 피 채워지는 애니메이션을 위해 Heal 리턴하고 애니메이션 출력예정.
    def __init__(self,type,Heal,Sell):
        item.__init__(type,Sell)
        self.Heal = Heal

    def Use_battle(self):
        return self.Heal

    def Use_daily(self):
        return self.Heal


class skill_machine(item):
    def __init__(self,type,Skill_Num,Sell):
        item.__init__(type,Sell)
        self.Skill_Num = Skill_Num
        self.Can_P = []

    def Use_battle(self):
        pass

    def Use_daily(self):
        return self.Heal
