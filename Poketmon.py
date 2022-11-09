import Skill_Data
from pico2d import *
import random
Poket_Data = None

class Data:
    image = None

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
        if Data.image == None:
            Data.image = load_image('All_Pokemon.png')

    def Front_Draw(self,x,y,width,height):
        self.image.clip_draw(self.Pngx,self.Pngy, 56, 56, x,y, width, height)

    def Back_Draw(self,x,y,width,height):
        self.image.clip_draw(self.Pngx + 8, self.Pngy -113,  48, 47, x, y, width, height)

class Poketmon:
    def __init__(self,Num,level,Hp,Skill_List):
        self.Num = Num
        self.level = level
        self.Hp = Hp
        self.Skill_List = Skill_List
        self.ailment = None

    def Set_ability(self):
        self.MaxHp =  (Poket_Data[self.Num].Hp * 2 + 31 + 100) * self.level // 100 + 10# [ { (종족값a x 2) + 개체값b + 100 } x 레벨Lv/100 ] + 10
        self.Pattack =   (Poket_Data[self.Num].Pattack * 2 + 31 + 100) * self.level // 100 + 5   # 능력치 = [ { (종족값a x 2) + 개체값b} x 레벨Lv/100 + 5]
        self.Pdefense = (Poket_Data[self.Num].Pdefense * 2 + 31 + 100) * self.level // 100 + 5
        self.Sattack = (Poket_Data[self.Num].Sattack * 2 + 31 + 100) * self.level // 100 + 5
        self.Sdefense = (Poket_Data[self.Num].Sdefense * 2 + 31 + 100) * self.level // 100 + 5
        self.Speed = (Poket_Data[self.Num].Speed* 2 + 31 + 100) * self.level // 100 + 5

    def ailment_check(self):
        if(self.ailment == 'Paralysis'):
            if(random.randint(0,100)<50):
                return 0
            else:
                return 1
        elif(self.ailment == 'Sleep'):
            if (random.randint(0, 100) < 50):
                self.ailment = None
                return 0
            else:
                return 1
        else:
            return 0

    def Type_check(self, Stype):
        sum = 1
        for Ptype in Poket_Data[self.Num].type:
            if Stype == 'Fight':                                # 기술이 격투
                if Ptype == 'Normal':
                    sum *= 2
                elif Ptype == 'Flight' or Ptype == 'Bug' or Ptype == 'Poison':
                    sum /= 2


            elif Stype == 'Water':                              # 기술이 물
                if Ptype == 'Fire':
                    sum *= 2
                elif Ptype == 'Water' or Ptype == 'Grass':
                    sum /= 2


            elif Stype == 'Fire':                               # 기술이 불
                if Ptype == 'Grass' or Ptype == 'Bug':
                    sum *= 2
                elif Ptype == 'Water' or Ptype == 'Fire':
                    sum /= 2


            elif Stype == 'Grass':                              # 기술이 풀
                if Ptype == 'Water':
                    sum *= 2
                elif Ptype == 'Poison' or Ptype == 'Flight' or Ptype == 'Bug':
                    sum /= 2


            elif Stype == 'Bug':
                if Ptype == 'Grass' or Ptype == 'Esper':
                    sum *= 2
                elif Ptype == 'Fight' or Ptype == 'Poison' or Ptype == 'Flight' or Ptype == 'Fire':
                    sum /= 2

            elif Stype == 'Poison':
                if Ptype == 'Poison':
                    sum /= 2
                elif Ptype == 'Grass':
                    sum *= 2

            elif Stype == 'Flight':
                if Ptype == 'Fight' or Ptype == 'Bug' or Ptype == 'Grass':
                    sum *= 2
                elif Ptype == 'Electric':
                    sum /= 2

            elif Stype == 'Electric':
                if Ptype == 'Flight' or Ptype == 'Water':
                    sum*=2
                elif Ptype == 'Electric' or Ptype == 'Grass':
                    sum /= 2
        return sum
    def init_Change_ability(self):                  # 전투시 능력치 변화 생성 함수
        self.ChangePa,self.ChangeSa,self.ChangePd,self.ChangeSd,self.ChangeSp = 0,0,0,0,0

    def del_Change_ability(self):                   # 전투 종료 또는 교체시 발동되는 능력치 변화 제거 함수
        del(self.ChangePa)
        del (self.ChangeSa)
        del (self.ChangePd)
        del (self.ChangeSd)
        del (self.ChangeSp)

    def Use_Skill(self,enermy,num,check):           # 공격모션 그릴때 check에 따라 그리기
        if (random.randint(0, 100) <= Skill_Data.Attack[self.Skill_List[num]].Daccur):
            Skill_Data.Attack[self.Skill_List[num]].Draw(check,enermy)
            Skill_Data.Attack[self.Skill_List[num]].Use(enermy,self)
            return 0
        else:
            return 8







class Wild_Poketmon(Poketmon):      # 트레이너 포켓몬 클래스
    def __init__(self,Num,level,Hp):
        Poketmon.__init__(self,Num,level,Hp,[])

    def Set_Skill(self):
        i = self.level
        while(i>0  and len(self.Skill_List)<4):
            if(i in Poket_Data[self.Num].Skill):
                self.Skill_List.append(Poket_Data[self.Num].Skill.get(i))
            i -= 1

        sorted(self.Skill_List)
        print(Poket_Data[self.Num].name,self.level)
        for i in self.Skill_List:
            print(Skill_Data.Attack[i])

        self.Hp = self.MaxHp

class Tr_Poketmon(Poketmon):
    def __init__(self, Num, level, Hp,Exp):
        Poketmon.__init__(self, Num, level, Hp, [])
        self.Exp = Exp


def init_Poketmon():
    global  Poket_Data
    Poket_Data = [Data(172, 2715,'Chikorita', 45, 49, 65, 49, 65, 45,16,['Grass'])]        # 치코리타
    Poket_Data.append(Data(343, 2715,'Bayleef', 60, 62, 80, 63, 80, 60,32,['Grass']))      # 베이리프
    Poket_Data.append(Data(514, 2715,'Meganium', 80, 82, 100, 83, 100, 80,101,['Grass']))   # 메가니움

    Poket_Data.append(Data(685, 2715, 'Cyndaquil', 39, 52, 43, 60, 50, 65,14, ['Fire']))   # 브케인
    Poket_Data.append(Data(856, 2715, 'Quilava', 58, 64, 58, 80, 65, 80,36, ['Fire']))     # 마그케인
    Poket_Data.append(Data(1027, 2715, 'Typhlosion', 78, 84, 78, 109, 85, 100,101, ['Fire']))   # 블레이범

    Poket_Data.append(Data(1198, 2715, 'Totodile', 50, 65, 64, 44, 48, 43,18, ['Water']))      # 리아코
    Poket_Data.append(Data(1369, 2715, 'Croconaw', 65, 80, 80, 59, 63, 58, 30, ['Water']))      # 엘리게이
    Poket_Data.append(Data(1540, 2715, 'Feraligatr', 85, 105, 100, 79, 83, 78, 101, ['Water']))  # 장크로다일

    Poket_Data.append(Data(1, 2527, 'Sentret', 35, 46, 34, 35, 45, 20, 15,['Normal']))     # 꼬리선
    Poket_Data.append(Data(172, 2527, 'Furret', 85, 76, 64, 45, 55, 90, 101,['Normal']))     # 다꼬리

    Poket_Data.append(Data(1540, 5535, 'Caterpie', 45, 30, 35, 20, 20, 45,7, ['Bug']))  # 캐터피
    Poket_Data.append(Data(1, 5290, 'Metapod', 50, 20, 55, 25, 25, 30, 10,['Bug']))  # 단데기
    Poket_Data.append(Data(172, 5290, 'Furret', 85, 76, 64, 45, 55, 90, 101,['Bug','Flight']))  # 버터플

    Poket_Data.append(Data(343, 5290, 'Weedle', 40, 35, 30, 20, 20, 50, 7,['Bug','Poison']))  # 뿔충이
    Poket_Data.append(Data(514, 5290, 'Kakuna', 45, 25, 50, 25, 25, 35, 10,['Bug','Poison']))  # 딱충이
    Poket_Data.append(Data(685, 5290, 'Beedrill', 65, 90, 40, 45, 80, 75, 101,['Bug','Poison']))  # 독침충

    Poket_Data.append(Data(856, 5290, 'Pidgey', 40, 45, 40, 35, 35, 56, 18,['Normal', 'Flight']))  # 구구
    Poket_Data.append(Data(1027, 5290, 'Pidgeotto', 63, 60, 55, 50, 50, 71,36, ['Normal', 'Flight']))  # 피죤
    Poket_Data.append(Data(1198, 5290, 'Pidgeot', 83, 80, 75, 70, 70, 101, 101,['Normal', 'Flight']))  # 피죤투

    Poket_Data.append(Data(685, 5159, 'Pikachu', 35, 55, 40, 50, 50, 90, 30,['Electric']))  # 피카츄
    Poket_Data.append(Data(856, 5159, 'Raichu', 60, 90, 55, 90, 80, 110, 101,['Electric']))  # 라이츄

    Poket_Data.append(Data(343, 2527, 'Hoothoot', 60, 30, 30, 36, 56, 50,20, ['Normal', 'Flight']))     # 부우부
    Poket_Data.append(Data(514, 2527, 'Noctowl', 100, 50, 50, 86, 96, 70, 101,['Normal', 'Flight']))     # 야부엉

    Poket_Data.append(Data(856, 4407, 'Machop', 70, 80, 50, 35, 35, 35, 28,['Fight']))  # 알통몬
    Poket_Data.append(Data(1027, 4407, 'Machoke', 80, 100, 70, 50, 60, 45, 40,['Fight']))  # 근육몬
    Poket_Data.append(Data(1198, 4407, 'Machamp', 90, 130, 80, 65, 85, 55, 101,['Fight']))  # 괴력몬


def init_Skill():
    Poket_Data[0].Skill = {1 : 0,2:1,8:2,13:3,20:4,28:5}
    Poket_Data[1].Skill = {1: 0, 2: 1, 8: 2, 13: 3, 20: 4, 28: 5}
    Poket_Data[2].Skill = {1 : 0,2:1,8:2,13:3,20:4,28:5}

    Poket_Data[3].Skill = {1: 0,2:9,10:6,17:7,25:8}
    Poket_Data[4].Skill = {1: 0, 2: 9, 10: 6, 17: 7, 25: 8}
    Poket_Data[5].Skill = {1: 0, 2: 9, 10: 6, 17: 7, 25: 8}

    Poket_Data[6].Skill = {1:10,2:9,7:11,13:12,20:13,27:14,32:15,43:16,52:17}
    Poket_Data[7].Skill = {1: 10, 2: 9, 7: 11, 13: 12, 20: 13, 27: 14, 32: 15, 43: 16, 52: 17}
    Poket_Data[8].Skill = {1: 10, 2: 9, 7: 11, 13: 12, 20: 13, 27: 14, 32: 15, 43: 16, 52: 17}

    Poket_Data[9].Skill = {1:0,2:1,11:7,20:18,25:13,33:19}
    Poket_Data[10].Skill = {1: 0, 2: 1, 11: 7, 20: 18, 25: 13, 33: 19}

    Poket_Data[11].Skill = {1:0,2:20}
    Poket_Data[12].Skill = {1: 0, 7: 21}
    Poket_Data[13].Skill = {1: 0, 2: 20,10:22,13:3,14:23,15:24,28:25,34:26}

    Poket_Data[14].Skill = {1: 27, 2: 20}
    Poket_Data[15].Skill = {1: 0, 7: 21}
    Poket_Data[16].Skill = {1: 27, 2: 20,15:11,25:29,30:30}

    Poket_Data[17].Skill = {1: 0, 2: 1, 9: 25, 15: 7, 25: 31}
    Poket_Data[18].Skill = {1: 0, 2: 1, 9: 25, 15: 7, 25: 31}
    Poket_Data[19].Skill = {1: 0, 2: 1, 9: 25, 15: 7, 25: 31}

    Poket_Data[20].Skill = {1: 32,2:1,6:33,8:34,11:7,20:18,26:35,41:36}
    Poket_Data[21].Skill = {1: 32, 2: 1, 6: 33, 8: 34, 11: 7, 20: 18, 26: 35, 41: 36}

    Poket_Data[22].Skill = {1: 0, 2: 1,10:37,16:38,20:39,25:34,30:25}
    Poket_Data[23].Skill = {1: 0, 2: 1, 10: 37, 16: 38,20:39, 25: 34,30:25}

    Poket_Data[24].Skill = {1:40,2:9,10:41,17:42,25:14,30:43}
    Poket_Data[25].Skill = {1: 40, 2: 9, 10: 41, 17: 42, 25: 14, 30: 43}
    Poket_Data[26].Skill = {1: 40, 2: 9, 10: 41, 17: 42, 25: 14, 30: 43}