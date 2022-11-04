import random

Skill_Data = None


class P_Skill:
    def __init__(self,Damage,Daccur,Maxpp,type):
        self.Damage = Damage
        self.Daccur = Daccur
        self.Maxpp = Maxpp
        self.type = type

    def Use(self,My,Enermy):
        if(random.randint(0,100)<=self.Daccur):
            print(Enermy.ChangePa)
            print(My.Hp)
            My.Hp = My.Hp - int((self.Damage * Enermy.Pattack * (1 + 1/4 * Enermy.ChangePa) * (Enermy.level * 2 / 5 + 2) / My.Pdefense * (1 + 1/4 * My.ChangePd) /50 + 2)* My.Type_check(self.type))
            print(My.Hp)
        else:
            print('Miss')

class S_Skill:
    def __init__(self,Damage,Daccur,Maxpp,type):
        self.Damage = Damage
        self.Daccur = Daccur
        self.Maxpp = Maxpp
        self.type = type

    def Use(self,My,Enermy):
        if(random.randint(0,100)<=self.Daccur):
            print(Enermy.ChangePa)
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))




class body_blow(P_Skill):                 # 몸통박치기
    def __init__(self):
        P_Skill.__init__(self,40,100,35,'Normal')


class crying_sound:             # 울음소리
    def __init__(self):
        self.PPowerbuf = -1
        self.Maxpp = 35,
        self.Daccur = 100
        self.type = 'Normal'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if(My.ChangePa >-3):
                My.ChangePa -= 1

class Razor_Leaf(S_Skill):               # 잎날가르기

    def __init__(self):
        S_Skill.__init__(self, 55, 95, 25, 'Grass')


class Poison_Powder:            # 독가루
    def __init__(self):
        self.Daccur = 75
        self.Maxpp = 25
        self.type = 'Grass'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if(My.ailment == None):
                My.ailment = 'Poison'

class Synthesis:                # 광합성
    def __init__(self):
        self.Hill = 100
        self.Maxpp = 5
        self.type = 'Grass'

    def Use(self):
        pass

class Body_Slam(P_Skill):            # 누르기
    def __init__(self):
        P_Skill.__init__(self, 85, 100, 15, 'Normal')


class Ember(S_Skill):                # 불꽃세례
    def __init__(self):
        S_Skill.__init__(self, 40, 100, 25, 'Fire')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10 and My.ailment == None):
                My.ailment = 'Burn'

class Quick_Attack(P_Skill):         # 전광석화
    def __init__(self):
        P_Skill.__init__(self, 40, 100, 30, 'Normal')


class Flame_Wheel(P_Skill):          # 화염자동차
    def __init__(self):
        P_Skill.__init__(self, 60, 100, 25, 'Fire')
    def Use(self,My,Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Pattack * (1 + 1 / 4 * Enermy.ChangePa) * (Enermy.level * 2 / 5 + 2) / My.Pdefense * (1 + 1 / 4 * My.ChangePd) / 50 + 2) * My.Type_check(self.type))
            if(random.randint(0,100)<10 and My.ailment == None):
                My.ailment = 'Burn'

class Leer:                 # 째려보기
    def __init__(self):
        self.PDefensebuf = -1
        self.Maxpp = 35
        self.type = 'Normal'
        self.Daccur = 100

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (My.ChangePd > -3):
                My.ChangePd -= 1

class Scratch(P_Skill):              # 할퀴기
    def __init__(self):
        P_Skill.__init__(self, 40, 100, 35, 'Normal')

class Rage(P_Skill):                 # 분노
    def __init__(self):
        P_Skill.__init__(self, 20, 100, 20, 'Normal')


class Water_Gun(S_Skill):            # 물대포
    def __init__(self):
        S_Skill.__init__(self, 40, 100, 25, 'Water')


class Bite(P_Skill):                 # 물기
    def __init__(self):
        P_Skill.__init__(self, 60, 100, 25, 'Dark')

class Scary_Face:           # 겁나는 얼굴
    def __init__(self):
        self.Speedbuf = -2
        self.Maxpp = 10
        self.Daccur = 90
        self.type = 'Normal'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (My.ChangeSp > -2):
                My.ChangeSp -= 2

class Slash(P_Skill):                # 베어가르기
    def __init__(self):
        P_Skill.__init__(self, 70, 100, 20, 'Normal')

class Screech:              # 싫은소리
    def __init__(self):
        self.PDefensebuf = -2
        self.Maxpp = 40
        self.Daccur = 85
        self.type = 'Normal'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (My.ChangePd > -2):
                My.ChangePd -= 2

class Hydro_Pump(S_Skill):           # 하이드로펌프
    def __init__(self):
        S_Skill.__init__(self, 120, 80, 5, 'Water')

class Slam(P_Skill):                 # 힘껏치기
    def __init__(self):
        P_Skill.__init__(self, 80, 75, 20, 'Normal')


class Amnesia:              # 망각술
    def __init__(self):
        self.SDefensebuf = 2
        self.Maxpp = 20
        self.Daccur
        self.type = 'Esper'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (Enermy.ChangeSd < 2):
                Enermy.ChangeSd += 2

class String_Shot:          # 실뿜기
    def __init__(self):
        self.Speedbuf = -2
        self.Maxpp = 20
        self.type = 'Bug'
        self.Daccur = 100

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (My.ChangeSp > -2):
                My.ChangeSp -= 2


class Harden:               # 단단해지기
    def __init__(self):
        self.PDefensebuf = 1
        self.Maxpp = 40
        self.type = 'Normal'
        self.Daccur

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (Enermy.ChangePd < 3):
                Enermy.ChangePd += 1

class Confusion(S_Skill):            # 염동력
    def __init__(self):
        S_Skill.__init__(self, 50, 100, 25, 'Esper')


class Stun_Spore:               # 저리가루
    def __init__(self):
        self.Maxpp = 15
        self.Daacur = 75
        self.type = 'Grass'

    def Use(self, My, Enermy):
        if (random.randint(0, 75) <= self.Daccur):
            if (My.ailment == None):
                My.ailment = 'Paralysis'


class Sleep_Powder:  # 수면가루
    def __init__(self):
        self.Maxpp = 15
        self.Daacur = 75
        self.type = 'Grass'

    def Use(self, My, Enermy):
        if (random.randint(0, 75) <= self.Daccur):
            if (My.ailment == None):
                My.ailment = 'Sleep'

class Gust(S_Skill):     # 바람일으키기
    def __init__(self):
        S_Skill.__init__(self, 40, 100, 35, 'Flight')


class Psybeam(S_Skill):  # 환상빔
    def __init__(self):
        S_Skill.__init__(self, 65, 100, 20, 'Esper')


class Poison_Sting(S_Skill):    # 독침
    def __init__(self):
        S_Skill.__init__(self, 15, 100, 35, 'Poison')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10):
                My.ailment = 'Poison'

class Agility:        # 고속이동
    def __init__(self):
        self.Speedbuf = 2
        self.Maxpp = 30
        self.type = 'Esper'
        self.Daccur

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (Enermy.ChangePd < 2):
                Enermy.ChangePd += 2

class Pursuit(P_Skill):        # 따라가때리기
    def __init__(self):
        P_Skill.__init__(self, 40, 100, 20, 'Dark')


class Pin_Missile(P_Skill):      # 바늘 미사일
    def __init__(self):
        P_Skill.__init__(self, 25, 95, 100, 'Bug')
    def Use(self,My,Enermy):
        i = random.randint(2,4)
        count  = 0
        while(count<i and random.randint(0,100)<=self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Pattack * (1 + 1/4 * Enermy.ChangePa) * (Enermy.level * 2 / 5 + 2) / My.Pdefense * (1 + 1/4 * My.ChangePd) /50 + 2)* My.Type_check(self.type))
            count+= 1
        pass

class Wing_Attack(P_Skill):     # 날개치기
    def __init__(self):
        P_Skill.__init__(self, 60, 100, 35, 'Bug')


class Thundershock:    # 전기쇼크
    def __init__(self):
        S_Skill.__init__(self, 40, 100, 30, 'Electric')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10):
                My.ailment = 'Paralysis'

class Tail_Whip:      # 꼬리 흔들기
    def __init__(self):
        self.PDefensebuf = -1
        self.Maxpp = 30
        self.type = 'Normal'
        self.Daccur

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if (Enermy.ChangePd > -2):
                Enermy.ChangePd -= 1

class Thunder_Wave:     # 전기 충격파
    def __init__(self):
        self.Daccur = 90
        self.Maxpp = 20
        self.type = 'Electric'

    def Use(self, My, Enermy):
        if (random.randint(0, 90) <= self.Daccur):
            if (My.ailment == None):
                My.ailment = 'Paralysis'

class Thunderbolt(S_Skill):      # 10만볼트
    def __init__(self):
        S_Skill.__init__(self, 90, 100, 15, 'Electric')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10):
                My.ailment = 'Paralysis'

class Thunder(S_Skill):          # 번개
    def __init__(self):
        S_Skill.__init__(self, 110, 70, 10, 'Electric')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10):
                My.ailment = 'Paralysis'


class Peck(P_Skill):             # 쪼기
    def __init__(self):
        P_Skill.__init__(self, 35, 100, 35, 'Flight')


class Hypnosis:         # 최면술
    def __init__(self):
        self.Daacur = 60
        self.Maxpp = 20
        self.type = 'Esper'

    def Use(self, My, Enermy):
        if (random.randint(0, 90) <= self.Daccur):
            if (My.ailment == None):
                My.ailment = 'Sleep'

class Take_Down(P_Skill):        # 돌진
    def __init__(self):
        P_Skill.__init__(self, 90, 85, 20, 'Normal')


class Low_Kick(P_Skill):         # 안다리걸기
    def __init__(self):
        P_Skill.__init__(self, 40, 100, 30, 'Fight')


class Karate_Chop(P_Skill):      # 태권당수
    def __init__(self):
        P_Skill.__init__(self, 70, 100, 25, 'Fight')


class Cross_Chop(P_Skill):       # 크로스춉
    def __init__(self):
        P_Skill.__init__(self, 100, 80, 5, 'Fight')


class Submission(P_Skill):       # 지옥의 바퀴
    def __init__(self):
        P_Skill.__init__(self, 80, 80, 25, 'Fight')


def init_skill():
    global Skill_Data





Attack = [body_blow(),crying_sound(),Razor_Leaf(),Poison_Powder(),Synthesis(),Body_Slam(),
          Ember(), Quick_Attack(),Flame_Wheel(),Leer(),Scratch(),Rage(),Water_Gun(),
          Bite(),Scary_Face(),Slash(),Screech(),Hydro_Pump(),Slam(),Amnesia(),
          String_Shot(),Harden(),Confusion(),Stun_Spore(),Sleep_Powder(),Gust(),
          Psybeam(),Poison_Sting(),Agility(),Pursuit(),Pin_Missile(),Wing_Attack(),
          Thundershock(),Tail_Whip(),Thunder_Wave(),Thunderbolt(),Thunder(),Peck(),
          Hypnosis(),Take_Down(),Low_Kick(),Karate_Chop(),Cross_Chop(),Submission()]       # Attack라는 리스트에 body_blow,crying_sound라는 string을 넣은 후

def Use_Skill(play):
    print(play,Attack[play])
    Attack[play].Use()                  # Attack의 0번쨰 인덱스인 body_blow.Use()를 불러옴
                                        # self인자 없다는 오류가 발생함
                                        # 32번째 줄과 41번째 줄 참고




