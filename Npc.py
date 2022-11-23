import Character
from Map import Maping
import Poketmon
import game_framework
import play_state
import Font
import wild_Battle

class Npc(Character.character):
    def __init__(self,pngx,pngy,height,weight,mapx,mapy):
        Character.character.__init__(self,pngx,pngy,height,weight,mapx,mapy)
        self.Dialog_1 = None
        self.Dialog_2 = None
        self.Met = False
        self.Dia_Count = 0
    def return_Diag(self):
        if(not(self.Met)):
            if(len(self.Dialog_1)== self.Dia_Count):
                self.Dia_Count = 0
                self.End_Diag()

            else:
                self.Dia_Count += 1

        else:
            if (len(self.Dialog_2) == self.Dia_Count):
                self.Dia_Count = 0
                self.End_Diag()

            else:
                self.Dia_Count += 1


    def End_Diag(self):
        game_framework.pop_state()

    def Draw(self):
        if(not(self.Met)):
            Font.Draw_Al(*self.Dialog_1[self.Dia_Count - 1], 60, 75, 16, 16)
        else:
            Font.Draw_Al(*self.Dialog_2[self.Dia_Count - 1], 60, 75, 16, 16)

class Battle_Npc(Npc):
    def __init__(self, pngx, pngy, height, weight, mapx, mapy,Pcount):
        Npc.__init__(self,pngx,pngy,height,weight,mapx,mapy)
        self.Pcount = Pcount
        self.Poket = []

    def End_Diag(self):
        wild_Battle.Battle_type = 'Trainer'
        game_framework.change_state(wild_Battle)

class Given_Npc(Npc):
    def __init__(self, pngx, pngy, height, weight, mapx, mapy,kind,Num,count):
        Npc.__init__(self, pngx, pngy, height, weight, mapx, mapy)
        self.kind = kind
        self.Num = Num
        self.count = count

    def End_Diag(self):
        if(self.kind  == 0):
            pass
        elif(self.kind == 1):
            print(play_state.hero.inventory.Ball[self.Num][1])
            play_state.hero.inventory.Ball[self.Num][1] += self.count
        elif(self.kind == 2):
            pass
        else:
            play_state.hero.inventory.Riding = True
        self.Met = True
        game_framework.pop_state()



class Salesman(Npc):
    def _init__(self,pngx,pngy,height,weight,mapx,mapy):
        Npc._init__(self,pngx,pngy,height,weight,mapx,mapy)

class Healer(Npc):
    def _init__(self,pngx,pngy,height,weight,mapx,mapy):
        Npc._init__(self,pngx,pngy,height,weight,mapx,mapy)


Maping[1].Npccount = 1
Maping[1].Npc = [Npc(154, 2261, 32, 32, 336, 208) for i in range(0, 1)]  # 트레이너


Maping[3].Npccount = 1
Maping[3].Npc = [Npc(154, 2261, 32, 32, 528, 80) for i in range(0, 1)]  #트레이너
Maping[3].Npc.append(Npc(290, 3044, 32, 32, 560, 240))

Maping[6].Npccount = 1
Maping[6].Npc = [Npc(51, 3111, 32, 32, 304, 208) for i in range(0, 1)]  # 어무니
Maping[6].Npc[0].Dialog_1 = [['Jiu Go to Professor House'],['and Get your Pokemon']]
# Maping[6].Npc[0].Poket.append(Poketmon.Wild_Poketmon(1,10,10)),Maping[6].Npc[0].Poket.append(Poketmon.Wild_Poketmon(4,10,10))


Maping[7].Npccount = 3
Maping[7].Npc = [Npc(52, 3213, 32, 32, 304, 464) for i in range(0, 1)]  #박사님
Maping[7].Npc[0].Dialog_1 = [['Hi Jiu Today select your Pokemon'],['choose from the right']]

Maping[7].Npc.append(Given_Npc(290, 3044, 32, 32, 272, 16,1,0,5))                   #조교
Maping[7].Npc[1].Dialog_1 = [['Hi Jiu'],['This MonsterBall give to you']]
Maping[7].Npc[1].Dialog_2 = [['Good Travel Jiu']]

Maping[7].Npc.append(Npc(222, 3044, 32, 32, 464, 176))                   #조교
Maping[7].Npc[2].Dialog_1 = [['Good Travel Jiu']]


Maping[8].Npccount = 1
Maping[8].Npc = [Given_Npc(154, 2635, 32, 32, 304, 464,2,0,1) for i in range(0, 1)]  #할아버지
Maping[8].Npc[0].Dialog_1 = [['Do you want to take the spray']]

Maping[9].Npccount = 1
Maping[9].Npc = [Npc(289, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #아줌마
Maping[9].Npc[0].Dialog_1 = [['Stop asking for food']]

Maping[9].Npc.append(Npc(222, 2566, 32, 32, 368, 304))
Maping[9].Npc[1].Dialog_1 = [['Im hungry Give me food']]                # 아저씨


Maping[10].Npccount = 1
Maping[10].Npc = [Npc(224, 3146, 32, 32, -50, -50) for i in range(0, 1)]  #할아버지
Maping[10].Npc[0].Dialog_1 = [['Im hungry Give me foodddddd']]

Maping[11].Npccount = 1
Maping[11].Npc = [Npc(154, 3077, 32, 32, 336, 336) for i in range(0, 1)]  #할아버지
Maping[11].Npc[0].Dialog_1 = [['Im hungry Give me food']]

Maping[12].Npccount = 1
Maping[12].Npc = [Npc(289, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지
Maping[12].Npc[0].Dialog_1 = [['Im hungry Give me food']]

Maping[13].Npccount = 1
Maping[13].Npc = [Healer(18, 2908, 32, 32, 80, 464) for i in range(0, 1)]  #간호순

Maping[14].Npccount = 1
Maping[14].Npc = [Salesman(290, 2839, 32, 32, 144, 304) for i in range(0, 1)]  #마트 판매원

Maping[20].Npccount = 1
Maping[20].Npc = [Npc(18, 2908, 32, 32, 272, 368) for i in range(0, 1)]  #마트판매원

Maping[21].Npccount = 1
Maping[21].Npc = [Npc(290, 2839, 32, 32, 176, 304) for i in range(0, 1)]  #간호순

Maping[22].Npccount = 1
Maping[22].Npc = [Npc(290, 2601, 32, 32, 240, 208) for i in range(0, 1)]  #할아버지
Maping[22].Npc.append(Npc(222, 1377, 32, 32, 400, 272))
Maping[22].Npc.append(Npc(222, 2601, 32, 32, 400, 336))
Maping[22].Npc.append(Npc(52, 1682, 32, 32, 304, 464))

Maping[23].Npccount = 1
Maping[23].Npc = [Npc(154, 1275, 32, 32, 272, 176) for i in range(0, 1)]  #할아버지
Maping[23].Npc.append(Npc(18, 1037, 32, 32, 304, 496))
Maping[23].Npc.append(Npc(154, 1513, 32, 32, 368, 368))
Maping[23].Npc.append(Npc(154, 2023, 32, 32, 368, 240))

Maping[25].Npccount = 1
Maping[25].Npc = [Npc(290, 2635, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지
Maping[25].Npc.append(Npc(222, 2328, 32, 32, 368, 272))                   #할머니





