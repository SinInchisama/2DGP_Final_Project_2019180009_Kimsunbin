Poket_Data = None

class Poketmon:
    def __init__(self, Pngx, Pngy,name,Hp,Pattack,Pdefense,Sattack,Sdefense,Speed,Evolution,type):         # 이 클래스에 skill를 넣을 건데
        self.Pngx = Pngx                                                                                # 이때 딕셔너리 구조로 {1 : skill인덱스}로 찾을려고함
        self.Pngy = Pngy
        self.name = name
        self.Hp = Hp
        self.Pattack = Pattack
        self.Pdefense = Pdefense
        self.Sattack = Sattack
        self.Sdefense = Sdefense
        self.Speed = Speed
        self.Evolution = Evolution
        self.type = type

class Tr_Poketmon:      # 트레이너 포켓몬 클래스
    def __init__(self,Num,level,MaxHp,Hp,Pattack,Pdefense,Sattack,Sdefense,Speed,Nowexp):
        self.Num = Num
        self.level = level
        self.MaxHp = MaxHp
        self.Hp = Hp
        self.Pattack = Pattack
        self.Pdefense = Pdefense
        self.Sattack = Sattack
        self.Sdefense = Sdefense
        self.Speed = Speed
        self.Nowexp = Nowexp

    def Set_ability(self):
        # RHp =   (Poket_Data[self.Num].Hp * 2 + 31 + 100) * self.level // 100 + 10# [ { (종족값a x 2) + 개체값b + 100 } x 레벨Lv/100 ] + 10
        RPattack =   (Poket_Data[self.Num].Pattack * 2 + 31 + 100) * self.level // 100 + 5   # 능력치 = [ { (종족값a x 2) + 개체값b} x 레벨Lv/100 + 5]
        RPdefense = (Poket_Data[self.Num].Pdefense * 2 + 31 + 100) * self.level // 100 + 5
        RSattack = (Poket_Data[self.Num].Sattack * 2 + 31 + 100) * self.level // 100 + 5
        RSdefense = (Poket_Data[self.Num].Sdefense * 2 + 31 + 100) * self.level // 100 + 5
        RSpeed = (Poket_Data[self.Num].Speed* 2 + 31 + 100) * self.level // 100 + 5
        return RPattack,RPdefense,RSattack,RSdefense,RSpeed


def init_Poketmon():
    global  Poket_Data
    Poket_Data = [Poketmon(172, 2715,'Chikorita', 45, 49, 65, 49, 65, 45,16,['Grass'])]        # 치코리타
    Poket_Data.append(Poketmon(343, 2715,'Bayleef', 60, 62, 80, 63, 80, 60,32,['Grass']))      # 베이리프
    Poket_Data.append(Poketmon(514, 2715,'Meganium', 80, 82, 100, 83, 100, 80,101,['Grass']))   # 메가니움

    Poket_Data.append(Poketmon(685, 2715, 'Cyndaquil', 39, 52, 43, 60, 50, 65,14, ['Fire']))   # 브케인
    Poket_Data.append(Poketmon(856, 2715, 'Quilava', 58, 64, 58, 80, 65, 80,36, ['Fire']))     # 마그케인
    Poket_Data.append(Poketmon(1027, 2715, 'Typhlosion', 78, 84, 78, 109, 85, 100,101, ['Fire']))   # 블레이범

    Poket_Data.append(Poketmon(1198, 2715, 'Totodile', 50, 65, 64, 44, 48, 43,18, ['Water']))      # 리아코
    Poket_Data.append(Poketmon(1369, 2715, 'Croconaw', 65, 80, 80, 59, 63, 58, 30, ['Water']))      # 엘리게이
    Poket_Data.append(Poketmon(1540, 2715, 'Feraligatr', 85, 105, 100, 79, 83, 78, 101, ['Water']))  # 장크로다일

    Poket_Data.append(Poketmon(1, 2527, 'Sentret', 35, 46, 34, 35, 45, 20, 15,['Normal']))     # 꼬리선
    Poket_Data.append(Poketmon(172, 2527, 'Furret', 85, 76, 64, 45, 55, 90, 101,['Normal']))     # 다꼬리

    Poket_Data.append(Poketmon(1540, 5535, 'Caterpie', 45, 30, 35, 20, 20, 45,7, ['Bug']))  # 캐터피
    Poket_Data.append(Poketmon(1, 5290, 'Metapod', 50, 20, 55, 25, 25, 30, 10,['Bug']))  # 단데기
    Poket_Data.append(Poketmon(172, 5290, 'Furret', 85, 76, 64, 45, 55, 90, 101,['Bug','Flight']))  # 버터플

    Poket_Data.append(Poketmon(343, 5290, 'Weedle', 40, 35, 30, 20, 20, 50, 7,['Bug','Poison']))  # 뿔충이
    Poket_Data.append(Poketmon(514, 5290, 'Kakuna', 45, 25, 50, 25, 25, 35, 10,['Bug','Poison']))  # 딱충이
    Poket_Data.append(Poketmon(685, 5290, 'Beedrill', 65, 90, 40, 45, 80, 75, 101,['Bug','Poison']))  # 독침충

    Poket_Data.append(Poketmon(856, 5290, 'Pidgey', 40, 45, 40, 35, 35, 56, 18,['Normal', 'Flight']))  # 구구
    Poket_Data.append(Poketmon(1027, 5290, 'Pidgeotto', 63, 60, 55, 50, 50, 71,36, ['Normal', 'Flight']))  # 피죤
    Poket_Data.append(Poketmon(1198, 5290, 'Pidgeot', 83, 80, 75, 70, 70, 101, 101,['Normal', 'Flight']))  # 피죤투

    Poket_Data.append(Poketmon(685, 5159, 'Pikachu', 35, 55, 40, 50, 50, 90, 30,['Electric']))  # 피카츄
    Poket_Data.append(Poketmon(856, 5159, 'Raichu', 60, 90, 55, 90, 80, 110, 101,['Electric']))  # 라이츄

    Poket_Data.append(Poketmon(343, 2527, 'Hoothoot', 60, 30, 30, 36, 56, 50,20, ['Normal', 'Flight']))     # 부우부
    Poket_Data.append(Poketmon(514, 2527, 'Noctowl', 100, 50, 50, 86, 96, 70, 101,['Normal', 'Flight']))     # 야부엉

    Poket_Data.append(Poketmon(856, 4407, 'Machop', 70, 80, 50, 35, 35, 35, 28,['Fighting']))  # 알통몬
    Poket_Data.append(Poketmon(1027, 4407, 'Machoke', 80, 100, 70, 50, 60, 45, 40,['Fighting']))  # 근육몬
    Poket_Data.append(Poketmon(1198, 4407, 'Machamp', 90, 130, 80, 65, 85, 55, 101,['Fighting']))  # 괴력몬






