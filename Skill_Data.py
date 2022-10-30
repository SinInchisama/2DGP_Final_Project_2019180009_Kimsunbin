Skill_Data = None

class Dbuf:
    def __init__(self):         # buf가 양수면 그만큼 능력치가 상승함, 상태이상은 TRUE,FALSE로 판단
        self.PPowerbuf = 0
        self.SPowerbuf = 0
        self.PDefensebuf = 0
        self.SDefensebuf = 0
        self.Speedbuf = 0
        self.Poison = False
        self.Paralysis = False
        self.Sleep = False
        self.Burn = False

class Skill:
    def __init__(self,Daccur,Maxpp,type):
        Dbuf.__init__(self)
        self.Daccur = 100         # 기술마다 적중률
        self.Maxpp = Maxpp          # 기술 사용가능 횟수 최대값
        self.type = type            # 포켓몬 기술타입
        self.Damage = 0             # 말그대로 데미지
        self.Hill = 0               # 힐하는 스킬에 적용
        self.DBufaccur = 10          # 특정하지 않는 경우 상태이상 적중률은 10%
        self.Me = False             # 스킬이 나한테 써지는지 판단하는 변수 보통은 false

class body_blow:                 # 몸통박치기
    def __init__(self):
        self.Damage = 100
        self.Daccur = 95
        self.Maxpp = 35
        self.type = 'Normal'
    def Use(self):
        print(self.Damage)

class crying_sound:             # 울음소리
    def __init__(self):
        self.PPowerbuf = -1
        self.Maxpp = 35,
        self.type = 'Normal'

    def Use(self):
        pass

class Razor_Leaf:               # 잎날가르기
    def __init__(self):
        self.Damge = 55
        self.Daccur = 95
        self.Maxpp = 25
        self.type = 'Grass'

    def Use(self):
        pass

class Poison_Powder:            # 독가루
    def __init__(self):
        self.Daccur = 75
        self.Maxpp = 25
        self.type = 'Grass'

    def Use(self):
        pass

class Synthesis:                # 광합성
    def __init__(self):
        self.Hill = 100
        self.Maxpp = 5
        self.type = 'Grass'

    def Use(self):
        pass

class Body_Slam:
    def __init__(self):
        self.Damage = 85
        self.Maxpp = 15
        self.type = 'Normal'

    def Use(self):
        pass

class Ember:                # 불꽃세례
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 25
        self.type = 'Fire'

    def Use(self):
        pass

class Quick_Attack:         # 전광석화
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 30
        self.type = 'Normal'

    def Use(self):
        pass

class Flame_Wheel:          # 화염자동차
    def __init__(self):
        self.Damage = 60
        self.Maxpp = 25
        self.type = 'Fire'

    def Use(self):
        pass

class Leer:                 # 째려보기
    def __init__(self):
        self.PDefensebuf = -1
        self.Maxpp = 35
        self.type = 'Normal'

    def Use(self):
        pass

class Scratch:              # 할퀴기
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 35
        self.type = 'Normal'

    def Use(self):
        pass

class Rage:                 # 분노
    def __init__(self):
        self.Damage = 20
        self.Maxpp = 20
        self.type = 'Normal'
    def Use(self):
        pass

class Water_Gun:            # 물대포
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 25
        self.type = 'Water'
    def Use(self):
         pass

class Bite:                 # 물기
    def __init__(self):
        self.Damage = 60
        self.Maxpp = 25
        self.type = 'Water'

    def Use(self):
        pass

class Scary_Face:           # 겁나는 얼굴
    def __init__(self):
        self.Speedbuf = -2
        self.Maxpp = 10
        self.Daccur = 90
        self.type = 'Normal'
    def Use(self):
        pass

class Slash:                # 베어가르기
    def __init__(self):
        self.Damage = 70
        self.Maxpp = 20
        self.type = 'Normal'
    def Use(self):
        pass

class Screech:              # 싫은소리
    def __init__(self):
        self.PDefensebuf = -2
        self.Maxpp = 40
        self.Daccur = 85
        self.type = 'Normal'
    def Use(self):
        pass

class Hydro_Pump:           # 하이드로펌프
    def __init__(self):
        self.Damage = 120
        self.Maxpp = 5
        self.Daccur = 80
        self.tyoe = 'Water'
    def Use(self):
        pass

class Slam:                 # 힘껏치기
    def __init__(self):
        self.Damage = 80
        self.Maxpp = 20
        self.Daccur = 75
        self.type = 'Normal'
    def Use(self):
        pass

def init_skill():
    global Skill_Data
    Skill_Data = [Skill(0,0,None) for i in range(0,67)]
    Skill_Data[0].Damage,Skill_Data[0].Daccur,Skill_Data[0].Maxpp,Skill_Data[0].type = 35,95,35,'Normal'            # 몸통박치기
    Skill_Data[1].PPowerbuf, Skill_Data[1].Maxpp,Skill_Data[1].type  = -1, 35,'Normal'    # 울음소리
    Skill_Data[2].Damage,Skill_Data[2].Daccur,Skill_Data[2].Maxpp,Skill_Data[2].type = 55,95,25,'Grass'             # 잎날가르기
    Skill_Data[3].Poison, Skill_Data[3].Daccur, Skill_Data[3].Maxpp, Skill_Data[3].type,Skill_Data[3].DBufaccur = True, 75, 25, 'Grass',100  # 독가루
    Skill_Data[4].Hill,Skill_Data[4].Maxpp, Skill_Data[4].type, Skill_Data[4].Me = 100,5,'Grass',True       # 광합성
    Skill_Data[5].Damage,Skill_Data[5].Maxpp,Skill_Data[5].type = 85,15,'Normal'                            # 누르기
    Skill_Data[6].Damage,Skill_Data[6].Maxpp,Skill_Data[6].type,Skill_Data[8].Burn  = 40,25,'Fire',True             # 불꽃세례
    Skill_Data[7].Damage,Skill_Data[7].Maxpp,Skill_Data[7].type = 40,30,'Normal'                            # 전광석화
    Skill_Data[8].Damage,Skill_Data[8].Maxpp,Skill_Data[8].type,Skill_Data[8].Burn = 60,25,'Fire',True              # 화염자동차
    Skill_Data[9].PDefensebuf, Skill_Data[9].Maxpp, Skill_Data[9].type = -1, 35, 'Normal'  # 째려보기
    Skill_Data[10].Damage,Skill_Data[10].Maxpp,Skill_Data[10].type = 40,35,'Normal'         # 할퀴기
    Skill_Data[11].Damage, Skill_Data[11].Maxpp, Skill_Data[11].type = 20,20,'Normal'       # 분노
    Skill_Data[12].Damage, Skill_Data[12].Maxpp, Skill_Data[12].type = 40,25,'Water'        # 물대포
    Skill_Data[13].Damage, Skill_Data[13].Maxpp, Skill_Data[13].type = 60,25,'Evil'         # 물기
    Skill_Data[14].Speedbuf,Skill_Data[14].Maxpp,Skill_Data[14].Daccur,Skill_Data[14].type = -2,10,90,'Normal'      # 겁나는 얼굴
    Skill_Data[15].Damage, Skill_Data[15].Maxpp, Skill_Data[15].type = 70,20,'Normal'                               # 베어가르기
    Skill_Data[16].PDefensebuf,Skill_Data[16].Maxpp,Skill_Data[16].Daccur,Skill_Data[16].type = -2,40,85,'Normal'   # 싫은소리
    Skill_Data[17].Damage, Skill_Data[17].Maxpp,Skill_Data[17].Daccur, Skill_Data[17].type = 120, 5, 80, 'Water'    # 하이드로펌프

    Skill_Data[18].Damage, Skill_Data[18].Maxpp, Skill_Data[18].Daccur, Skill_Data[18].type = 80, 20, 75, 'Noraml'  # 힘껏치기
    Skill_Data[19].SDefensebuf,Skill_Data[19].Me,Skill_Data[19].Maxpp,Skill_Data[19].type = 2,True,20,'Esper'       # 망각술
    Skill_Data[20].Speedbuf,Skill_Data[20].Maxpp,Skill_Data[20].type = -1,20,'Bug'                                  # 실뿜기
    Skill_Data[21].PDefensebuf,Skill_Data[21].Me,Skill_Data[21].Maxpp,Skill_Data[21].type = 1,True,40,'Normal'      # 단단해지기
    Skill_Data[22].Damage, Skill_Data[22].Maxpp, Skill_Data[22].type = 50,25,'Esper'                                # 염동력
    Skill_Data[23].Paralysis,Skill_Data[23].Maxpp,Skill_Data[23].Daccur,Skill_Data[23].DBufaccur,Skill_Data[23].type = True,15,75,True,'Grass'
    Skill_Data[24].Sleep, Skill_Data[24].Maxpp, Skill_Data[24].Daccur, Skill_Data[24].DBufaccur, Skill_Data[24].type = True, 15, 75, True, 'Grass'
    Skill_Data[25].Damage, Skill_Data[25].Maxpp, Skill_Data[25].type = 40, 35, 'Flight'
    Skill_Data[26].Damage, Skill_Data[26].Maxpp, Skill_Data[26].type = 65, 20, 'Esper'
    Skill_Data[27].Damage, Skill_Data[27].Maxpp,Skill_Data[27].Poison, Skill_Data[27].type = 15,35,True,'Poison'



init_skill()

def Use_Skill(play):
   play.Use()

init_skill()
Use_Skill(Attack)
