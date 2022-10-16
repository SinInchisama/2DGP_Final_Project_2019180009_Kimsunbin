Poket_Data = None

class Poketmon:
    def __init__(self, Pngx, Pngy,name,Hp,MaxPattack,MaxPdefense,MaxSattack,MaxSdefense,Speed,type):         # 이 클래스에 skill를 넣을 건데
        self.Pngx = Pngx                                                                                # 이때 딕셔너리 구조로 {1 : skill인덱스}로 찾을려고함
        self.Pngy = Pngy
        self.name = name
        self.Hp = Hp
        self.MaxPattack = MaxPattack
        self.MaxPdefense = MaxPdefense
        self.MaxSattack = MaxSattack
        self.MaxSdefense = MaxSdefense
        self.Speed = Speed
        self.type = type

class Tr_Poketmon:      # 트레이너 포켓몬 클래스
    def __init__(self,Num,Hp,Pattack,Pdefense,Sattack,Sdefense,Speed):
        self.Num = Num
        self.Hp = Hp
        self.Pattack = Pattack
        self.Pdefense = Pdefense
        self.Sattack = Sattack
        self.Sdefense = Sdefense
        self.Speed = Speed


def init_Poketmon():
    global  Poket_Data
    Poket_Data = [Poketmon(172, 2715,'Chikorita', 45, 49, 65, 49, 65, 45,['Grass'])]        # 치코리타
    Poket_Data.append(Poketmon(343, 2715,'Bayleef', 60, 62, 80, 63, 80, 60,['Grass']))      # 베이리프
    Poket_Data.append(Poketmon(514, 2715,'Meganium', 80, 82, 100, 83, 100, 80,['Grass']))   # 메가니움

    Poket_Data.append(Poketmon(685, 2715, 'Cyndaquil', 39, 52, 43, 60, 50, 65, ['Fire']))   # 브케인
    Poket_Data.append(Poketmon(856, 2715, 'Quilava', 58, 64, 58, 80, 65, 80, ['Fire']))     # 마그케인
    Poket_Data.append(Poketmon(1027, 2715, 'Typhlosion', 78, 84, 78, 109, 85, 100, ['Fire']))   # 블레이범

    Poket_Data.append(Poketmon(1198, 2715, 'Totodile', 50, 65, 64, 44, 48, 43, ['Water']))      # 리아코
    Poket_Data.append(Poketmon(1369, 2715, 'Croconaw', 65, 80, 80, 59, 63, 58, ['Water']))      # 엘리게이
    Poket_Data.append(Poketmon(1540, 2715, 'Feraligatr', 85, 105, 100, 79, 83, 78, ['Water']))  # 장크로다일

    Poket_Data.append(Poketmon(1, 2527, 'Sentret', 35, 46, 34, 35, 45, 20, ['Normal']))     # 꼬리선
    Poket_Data.append(Poketmon(172, 2527, 'Furret', 85, 76, 64, 45, 55, 90, ['Normal']))     # 다꼬리

    Poket_Data.append(Poketmon(1540, 5535, 'Caterpie', 45, 30, 35, 20, 20, 45, ['Bug']))  # 캐터피
    Poket_Data.append(Poketmon(1, 5290, 'Metapod', 50, 20, 55, 25, 25, 30, ['Bug']))  # 단데기
    Poket_Data.append(Poketmon(172, 5290, 'Furret', 85, 76, 64, 45, 55, 90, ['Bug','Flight']))  # 버터플

    Poket_Data.append(Poketmon(343, 5290, 'Weedle', 40, 35, 30, 20, 20, 50, ['Bug','Poison']))  # 뿔충이
    Poket_Data.append(Poketmon(514, 5290, 'Kakuna', 45, 25, 50, 25, 25, 35, ['Bug','Poison']))  # 딱충이
    Poket_Data.append(Poketmon(685, 5290, 'Beedrill', 65, 90, 40, 45, 80, 75, ['Bug','Poison']))  # 독침충


