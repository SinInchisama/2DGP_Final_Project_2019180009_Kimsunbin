class Poketmon:
    def __init__(self, Pngx, Pngy,name,Hp,MaxPattack,MaxPdefense,MaxSattack,MaxSdefense,Speed):
        self.Pngx = Pngx
        self.Pngy = Pngy
        self.name = name
        self.Hp = Hp
        self.MaxPattack = MaxPattack
        self.MaxPdefense = MaxPdefense
        self.MaxSattack = MaxSattack
        self.MaxSdefense = MaxSdefense
        self.Speed = Speed

class Tr_Poketmon:      # 트레이너 포켓몬 클래스
    def __init__(self,Num,Hp,Pattack,Pdefense,Sattack,Sdefense,Speed):
        self.Num = Num
        self.Hp = Hp
        self.Pattack = Pattack
        self.Pdefense = Pdefense
        self.Sattack = Sattack
        self.Sdefense = Sdefense
        self.Speed = Speed

Poket_Data = [Poketmon(172, 2715,'Chikorita', 45, 49, 65, 49, 65, 45)]
Poket_Data.append(Poketmon(343, 2715,'Bayleef', 60, 62, 80, 63, 80, 60))
Poket_Data.append(Poketmon(514, 2715,'Meganium', 80, 82, 100, 83, 100, 80))


