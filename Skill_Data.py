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
    def __init__(self,Damage,Hill,Daccur):
        Dbuf.__init__(self)
        self.Damage = Damage        # 말그대로 데미지
        self.Hill = Hill            # 힐하는 스킬에 적용
        self.Daccur =Daccur         # 기술마다 적중률
        self.Bufaccur = 10          # 특정하지 않는 경우 DBuf적중률은 10%
        self.Me = False             # 스킬이 나한테 써지는지 판단하는 변수 보통은 false

def init_skill():
    global Skill_Data
    Skill_Data = [Skill(0,0,0) for i in range(0,67)]

init_skill()
