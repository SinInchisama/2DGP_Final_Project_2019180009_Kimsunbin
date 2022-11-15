import random
from pico2d import *
import Font
class item:                 # 아이템 기본 클래스
    def __init__(self,type,Sell):
        self.type = type
        self.Sell = Sell



class ball(item):           # 몬스터볼 기본 클래스
    def __init__(self,type,Sell,daccur):
        item.__init__(self,type,Sell)
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
        ball.__init__(self,'Ball',100,50)
        self.name = 'Monster Ball'

class Super_Ball(ball):                 # 슈퍼볼
    def __init__(self):
        ball.__init__(self,'Ball',200,70)
        self.name = 'Super Ball'

class Hiper_Ball(ball):                 # 하이퍼볼
    def __init__(self):
        ball.__init__(self,'Ball',300,80)
        self.name = 'Hiper Ball'

class Master_Ball(ball):  # 마스터볼
    def __init__(self):
        ball.__init__(self,'Ball', 10000, 100)
        self.name = 'Master Ball'

                                        # 회복약
class heal(item):                       # 피 채워지는 애니메이션을 위해 Heal 리턴하고 애니메이션 출력예정.
    def __init__(self,type,Heal,Sell):
        item.__init__(self,type,Sell)
        self.Heal = Heal

    def Use_battle(self):
        return self.Heal

    def Use_daily(self):
        return self.Heal

class Potion(heal):                   # 상처약
    def __init__(self):
        heal.__init__(self,'heal',20,50)
        self.name = 'Potion'

class Super_Potion(heal):
    def __init__(self):
        heal.__init__(self,'heal',60,150) # 좋은 상처약
        self.name = 'Super Potion'

class Hyper_Potion(heal):
    def __init__(self):
        heal.__init__(self,'heal',120,500) # 고급 상처약
        self.name = 'Super Potion'

class  Full_Heal(item):
    def __init__(self):
        item.__init__(self,'heal',200)
        self.name = 'Full Heal'
    def Use_battle(self,Poke):
        if(Poke.ailment != None):
            Poke.ailment = None

    def Use_daily(self,Poke):
        if(Poke.ailment != None):
            Poke.ailment = None

class skill_machine(item):
    def __init__(self,type,Skill_Num,Sell):
        item.__init__(type,Sell)
        self.Skill_Num = Skill_Num
        self.Can_P = []

    def Use_battle(self):
        pass

    def Use_daily(self):
        return self.Heal

class inventory:            # 플레이어 인벤토리
    image = None
    def __init__(self):
        self.Ball = [[Monster_Ball(),90],[Super_Ball(),0],[Hiper_Ball(),0],[Master_Ball(),0]]
        self.Heal = [[Potion(),0],[Super_Potion(),0],[Hyper_Potion(),0],[Full_Heal(),0]]
        self.Skill_machine = dict()
        self.Riding = False                 # 라이딩에 사용할 함수.
        self.Use_type = ''                  # battle 사용이냐 평소 사용이냐
        self.Nowtype = 0
        self.Nowitem = 0
        if(inventory.image == None):
            inventory.image = load_image('./resource/image/inventory.png')

    def Draw(self,type):
        inventory.image.clip_draw(176,653,160,144,320,288,640,576)


        if(type == 0):              # 포션
            inventory.image.clip_draw(344, 773, 40, 24, 80, 428, 160, 96)
            inventory.image.clip_draw(344, 663, 40, 24, 80, 300, 160, 96)

            y = 0
            for i in self.Heal:
                Font.Draw_Al(i[0].name, 200, 500 - (y * 70), 24, 24)
                Font.Draw_Al('X', 550, 480 - (y * 70), 24, 24)
                Font.Draw_Num(i[1], 610, 480 - (y * 70), 24, 24)
                y += 1

        elif(type == 1):            # 볼가방
            inventory.image.clip_draw(344, 747, 40, 24, 80, 428, 160, 96)
            inventory.image.clip_draw(344, 637, 40, 24, 80, 300, 160, 96)

            y = 0
            for i in self.Ball:
                Font.Draw_Al(i[0].name,200,500 - (y*70),24,24)
                Font.Draw_Al('X', 550, 480 - (y * 70), 24, 24)
                Font.Draw_Num(i[1], 610, 480 - (y * 70), 24, 24)
                y+= 1

        elif (type == 2):
            inventory.image.clip_draw(344, 721, 40, 24, 80, 428, 160, 96)
            inventory.image.clip_draw(344, 611, 40, 24, 80, 300, 160, 96)

            if(self.Riding):
                Font.Draw_Al('Bicycle', 200, 500, 24, 24)
            pass
        elif(type == 3):
            inventory.image.clip_draw(344, 695, 40, 24, 80, 428, 160, 96)
            inventory.image.clip_draw(344, 585, 40, 24, 80, 300, 160, 96)
            pass



