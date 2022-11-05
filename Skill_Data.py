import random
from pico2d import *
from wild_Battle import *

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

    def Draw(self,check,My):
        for i in range(2,0,-1):
            clear_canvas()

            draw_world()
            if(check):          # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 500, 450,128,128)
            else:               # 아니면 상대
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 120, 200,128,128)
            delay(0.05)
            update_canvas()


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

    def Draw(self, check,My):
        for i in range(0, 5):
            clear_canvas()

            draw_world()
            if (check):  # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(144, 1316, 8, 8, 450, 450- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 460, 470- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 430, 480- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 550, 400- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 540, 420- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 520, 430- i*10, 32, 32)
            else:  # 아니면 상대
                Skill_Data.clip_draw(144, 1316, 8, 8, 70, 150- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 80, 170- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 50, 230- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 70, 150- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 80, 170- i*10, 32, 32)
                Skill_Data.clip_draw(144, 1316, 8, 8, 50, 230- i*10, 32, 32)
            delay(0.03)
            update_canvas()

class Razor_Leaf(S_Skill):               # 잎날가르기

    def __init__(self):
        S_Skill.__init__(self, 55, 95, 25, 'Grass')
    def Draw(self, check,My):
        for a in range(0,300,2):
            clear_canvas()
            i = a // 50
            draw_world()
            if (check):  # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 70+ a * 1.5, 150 + a, 32, 32)
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 80+ a* 1.5, 170 + a, 32, 32)
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 50+ a* 1.5, 230 + a, 32, 32)
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 170+ a* 1.5, 100 + a, 32, 32)
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 160+ a* 1.5, 120 + a, 32, 32)
                Skill_Data.clip_draw(131 + i * 12, 1932, 10, 10, 140+ a* 1.5, 130 + a, 32, 32)
            else:  # 아니면 상대
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 450 - a, 450 - a, 32, 32)
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 460 - a, 470 - a, 32, 32)
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 430 - a, 480 - a, 32, 32)
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 550 - a, 400 - a, 32, 32)
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 540 - a, 420 - a, 32, 32)
                Skill_Data.clip_draw(131 + i * 14, 1932, 10, 10, 520 - a, 430 - a, 32, 32)
            delay(0.01)
            update_canvas()


class Poison_Powder:            # 독가루
    def __init__(self):
        self.Daccur = 75
        self.Maxpp = 25
        self.type = 'Grass'

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            if(My.ailment == None):
                My.ailment = 'Poison'

    def Draw(self,check,My):
        if (My.ailment == None):
            for i in range(0, 2):
                clear_canvas()

                draw_world()
                if (check):  # check면 상대한테 공격들어옴
                    Skill_Data.clip_draw(131 + (31 * i), 341, 27, 15, 430, 470, 108, 60)
                else:  # 아니면 상대
                    Skill_Data.clip_draw(131 + (31 * i), 341, 27, 15, 50, 220, 108, 60)
                delay(0.1)
                update_canvas()

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

    def Draw(self,check,My):
        for i in range(2,0,-1):
            clear_canvas()

            draw_world()
            if(check):          # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 500, 450,128,128)
            else:               # 아니면 상대
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 120, 200,128,128)
            delay(0.05)
            update_canvas()


class Ember(S_Skill):                # 불꽃세례
    def __init__(self):
        S_Skill.__init__(self, 40, 100, 25, 'Fire')

    def Use(self, My, Enermy):
        if (random.randint(0, 100) <= self.Daccur):
            My.Hp = My.Hp - int((self.Damage * Enermy.Sattack * (1 + 1 / 4 * Enermy.ChangeSa) * (Enermy.level * 2 / 5 + 2) / My.Sdefense * (1 + 1 / 4 * My.ChangeSd) / 50 + 2) * My.Type_check(self.type))
            if (random.randint(0, 100) < 10 and My.ailment == None):
                My.ailment = 'Burn'

    def Draw(self, check, My):
        for a in range(0, 200, 2):
            clear_canvas()
            i = a // 50

            draw_world()
            if (check):  # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(67 - (22 * i), 1771, 18, 18, 120 + a * 1.5, 200 + a, 90, 90)
            else:  # 아니면 상대
                Skill_Data.clip_draw(67 - (22 * i), 1771, 18, 18, 500 - a * 1.5, 450 - a, 90, 90)
            delay(0.05)
            update_canvas()

class Quick_Attack(P_Skill):         # 전광석화
    def __init__(self):
        P_Skill.__init__(self, 40, 100, 30, 'Normal')

    def Draw(self,check,My):
        for i in range(2,0,-1):
            clear_canvas()

            draw_world()
            if(check):          # check면 상대한테 공격들어옴
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 500, 450,128,128)
            else:               # 아니면 상대
                Skill_Data.clip_draw(2 + (36 * i), 1937, 32, 32, 120, 200,128,128)
            delay(0.05)
            update_canvas()


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
        self.Daccur = 100
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
        self.Daccur = 100

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
        self.Daccur = 100

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
        self.Daccur = 100

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
    Skill_Data = load_image('./resource/image/Skill_image.png')





Attack = [body_blow(),crying_sound(),Razor_Leaf(),Poison_Powder(),Synthesis(),Body_Slam(),
          Ember(), Quick_Attack(),Flame_Wheel(),Leer(),Scratch(),Rage(),Water_Gun(),
          Bite(),Scary_Face(),Slash(),Screech(),Hydro_Pump(),Slam(),Amnesia(),
          String_Shot(),Harden(),Confusion(),Stun_Spore(),Sleep_Powder(),Gust(),
          Psybeam(),Poison_Sting(),Agility(),Pursuit(),Pin_Missile(),Wing_Attack(),
          Thundershock(),Tail_Whip(),Thunder_Wave(),Thunderbolt(),Thunder(),Peck(),
          Hypnosis(),Take_Down(),Low_Kick(),Karate_Chop(),Cross_Chop(),Submission()]       # Attack라는 리스트에 body_blow,crying_sound라는 string을 넣은 후






