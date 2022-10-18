Skill_Data = None

class Dbuf:
    def __init__(self,PPowerbuf,SPowerbuf,PDefensebuf,SDefensebuf,Speedbuf,Poison,Paralysis,Sleep,Burn):
        self.PPowerbuf = 0
        self.SPowerbuf = 0
        self.PDefensebuf = 0
        self.SDefensebuf = 0
        self.Speedbuf = 0
        self.Poison = 0
        self.Paralysis = 0
        self.Sleep = 0
        self.Burn = 0

class Skill:
    def __init__(self,Damage,Hill,Daccur,Bufaccur,PPowerbuf,SPowerbuf,PDefensebuf,SDefensebuf,Speedbuf,Poison,Paralysis,Sleep,Burn):
        Dbuf.__init__(self,PPowerbuf,SPowerbuf,PDefensebuf,SDefensebuf,Speedbuf,Poison,Paralysis,Sleep,Burn)
        self.Damage = Damage
        self.Hill = Hill
        self.Daccur =Daccur
        self.Bufaccur = 10

def init_skill():
    global Skill_Data
    Skill_Data = [Skill(0,0,0) for i in range(0,67)]

init_skill()