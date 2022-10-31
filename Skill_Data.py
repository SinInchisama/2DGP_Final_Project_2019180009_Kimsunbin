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

    def Use(self):                              # 이 Use 함수와
        print(self.Damage)

class crying_sound:             # 울음소리
    def __init__(self):
        self.PPowerbuf = -1
        self.Maxpp = 35,
        self.type = 'Normal'

    def Use(self):                              # 이 Use 함수를
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

class Body_Slam:            # 누르기
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
        self.type = 'Dark'

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

class Amnesia:              # 망각술
    def __init__(self):
        self.SDefensebuf = 2
        self.Maxpp = 20
        self.type = 'Esper'

    def Use(self):
        pass

class String_Shot:          # 실뿜기
    def __init__(self):
        self.Speedbuf = -2
        self.Maxpp = 20
        self.type = 'Bug'
    def Use(self):
        pass

class Harden:               # 단단해지기
    def __init__(self):
        self.PDefensebuf = 1
        self.Maxpp = 40
        self.type = 'Normal'
    def Use(self):
        pass

class Confusion:            # 염동력
    def __init__(self):
        self.Damage = 50
        self.Maxpp = 25
        self.type = 'Esper'
    def Use(self):
        pass

class Stun_Spore:               # 저리가루
    def __init__(self):
        self.Maxpp = 15
        self.Daacur = 75
        self.type = 'Grass'

    def Use(self):
        pass


class Sleep_Powder:  # 수면가루
    def __init__(self):
        self.Maxpp = 15
        self.Daacur = 75
        self.type = 'Grass'

    def Use(self):
        pass

class Gust:     # 바람일으키기
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 35
        self.type = 'Flight'
    def Use(self):
        pass

class Psybeam:  # 환상빔
    def __init__(self):
        self.Damage = 65
        self.Maxpp = 20
        self.type = 'Esper'
    def Use(self):
        pass

class Poison_Sting:    # 독침
    def __init__(self):
        self.Damage = 15
        self.Maxpp = 35
        self.type = 'Poison'
    def Use(self):
        pass

class Agility:        # 고속이동
    def __init__(self):
        self.Speedbuf = 2
        self.Maxpp = 30
        self.type = 'Esper'
    def Use(self):
        pass

class Pursuit:        # 따라가때리기
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 20
        self.type = 'Dark'
    def Use(self):
        pass

class Pin_Missile:      # 바늘 미사일
    def __init__(self):
        self.Damage = 25
        self.Maxpp = 20
        self.Daacur = 95
        self.type = 'Bug'
    def Use(self):
        pass

class Wing_Attack:     # 날개치기
    def __init__(self):
        self.Damage = 60
        self.Maxpp = 35
        self.type = 'Flight'

    def Use(self):
        pass

class Thundershock:    # 전기쇼크
    def __init__(self):
        self.Damage = 40
        self.Maxpp = 30
        self.type = 'Electric'

    def Use(self):
        pass

class Tail_Whip:      # 꼬리 흔들기
    def __init__(self):
        self.PDefensebuf = -1
        self.Maxpp = 30
        self.type = 'Normal'
    def Use(self):
        pass

class Thunder_Wave:     # 전기 충격파
    def __init__(self):
        self.Daccur = 90
        self.Maxpp = 20
        self.type = 'Electric'
    def Use(self):
        pass

class Thunderbolt:      # 10만볼트
    def __init__(self):
        self.Damage = 90
        self.Maxpp = 15
        self.type = 'Electric'
    def Use(self):
        pass

class Thunder:          # 번개
    def __init__(self):
        self.Damage = 110
        self.Maxpp = 10
        self.Daccur = 70
        self.type = 'Electric'
    def Use(self):
        pass

class Peck:             # 쪼기
    def __init__(self):
        self.Damage = 35
        self.Maxpp = 35
        self.type = 'Flight'
    def Use(self):
        pass

class Hypnosis:         # 최면술
    def __init__(self):
        self.Daacur = 60
        self.Maxpp = 20
        self.type = 'Esper'
    def Use(self):
        pass

class Take_Down:        # 돌진
    def __init__(self):
        self.Damage = 90
        self.Daccur = 85
        self.Maxpp = 20
        self.type = 'Normal'
    def Use(self):
        pass

class Low_Kick:         # 안다리걸기
    def __init__(self):
        self.Damage = 50
        self.Maxpp = 30
        self.type = 'Fight'

    def Use(self):
        pass

class Karate_Chop:      # 태권당수
    def __init__(self):
        self.Damage = 70
        self.Maxpp = 25
        self.type = 'Fight'

    def Use(self):
        pass

class Cross_Chop:       # 크로스춉
    def __init__(self):
        self.Damage = 100
        self.Maxpp = 5
        self.Daccur = 80
        self.type = 'Fight'

    def Use(self):
        pass

class Submission:       # 지옥의 바퀴
    def __init__(self):
        self.Damage = 80
        self.Daccur = 80
        self.Maxpp = 25
        self.type = 'Fight'

    def Use(self):
        pass

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

def Damage_check(Damage,type):
    import wild_Battle



Use_Skill(0)                            # Use_skill 함수에 0을 보내고
