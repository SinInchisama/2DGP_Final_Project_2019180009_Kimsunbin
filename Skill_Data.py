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
        self.DBufaccur = 10          # 특정하지 않는 경우 DBuf적중률은 10%
        self.Me = False             # 스킬이 나한테 써지는지 판단하는 변수 보통은 false

def init_skill():
    global Skill_Data
    Skill_Data = [Skill(0,0,None) for i in range(0,67)]
    Skill_Data[0].Damage,Skill_Data[0].Daccur,Skill_Data[0].Maxpp,Skill_Data[0].type = 35,95,35,'Normal'            # 몸통박치기
    Skill_Data[1].PPowerbuf, Skill_Data[1].Maxpp,Skill_Data[1].type  = -1, 35,'Normal'    # 울음소리
    Skill_Data[2].Damage,Skill_Data[2].Daccur,Skill_Data[2].Maxpp,Skill_Data[2].type = 55,95,25,'Grass'             # 잎날가르기
    Skill_Data[3].Poison, Skill_Data[3].Daccur, Skill_Data[3].Maxpp, Skill_Data[3].type,Skill_Data[3].DBufaccur = True, 75, 25, 'Grass',100  # 독가루
    Skill_Data[4].Hill,Skill_Data[4].Maxpp, Skill_Data[4].type, Skill_Data[4].Me = 100,5,'Grass',True       # 광합성
    Skill_Data[5].Damage,Skill_Data[5].Maxpp,Skill_Data[5].type = 85,15,'Normal'                            # 누르기
    Skill_Data[6].Damage,Skill_Data[6].Maxpp,Skill_Data[6].type = 40,25,'Fire'                              # 불꽃세례
    Skill_Data[7].Damage,Skill_Data[7].Maxpp,Skill_Data[7].type = 40,30,'Normal'                            # 전광석화
    Skill_Data[8].Damage,Skill_Data[8].Maxpp,Skill_Data[8].type = 60,25,'Fire'                      # 화염자동차



init_skill()
