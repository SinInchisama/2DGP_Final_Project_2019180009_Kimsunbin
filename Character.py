import pico2d

import Map
import Poketmon
import play_state

class character:
    def __init__(self,pngx,pngy,height,weight,mapx,mapy):       # battle npc,hero, give Npc 상속 위한 기본 클래스
        self.pngx = pngx
        self.pngy = pngy
        self.height = height
        self.weight = weight
        self.mapx = mapx
        self.mapy = mapy

class Hero(character):
    import Npc
    def __init__(self,pngx,pngy,height,weight,chx,chy,mapx,mapy,movex,movey):       # 이후 추가 예정
        character.__init__(self,pngx,pngy,height,weight,mapx,mapy)
        self.chx = chx
        self.chy = chy
        self.movex = movex
        self.movey = movey
        self.Movecheck = False
        self.dircet = 0

    def init_pList(self):
        self.Pcount = 2
        self.pList = [Poketmon.Tr_Poketmon(0,100,30,200) for i in range(0,7)]
        self.pList[0].Num = 3
        self.pList[0].level = 9
        self.pList[0].Set_ability()
        self.pList[0].Hp = self.pList[0].MaxHp
        self.pList[0].Exp = 440
        self.pList[0].Skill_List = [35,40,1,0]

        self.pList[1].Set_ability()

    def move_check(self,map_array):               # 후에 여기에 round 매개변수 추가해서 4에 접근할때나 포켓몬 나오는거 조정예정
        self.mapx += (self.movex * 32)
        self.mapy += (self.movey * 32)
        # print(self.movex,self.movey,self.mapx,self.mapy,self.chx,self.chy)
        # if (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 1 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 5):
        #     return 1
        # elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 15):
        #     return 2
        # elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 0 or map_array[self.mapy // 32 + 1][ self.mapx // 32 + 1] == 2 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 3):
        #     self.mapx -= (self.movex * 32)
        #     self.mapy -= (self.movey * 32)
        #     return 0
        # print(map_array[self.mapy // 32 + 1][self.mapx // 32 + 1],self.mapy // 32 + 1,self.mapx // 32 + 1)
        check_num = map_array[self.mapy // 32 + 1][self.mapx // 32 + 1]
        if(check_num  == 89 or check_num  == 45 or check_num  == 32):
            return 2
        elif (check_num==149):
            return 3
        elif(check_num <=144):
            self.mapx -= (self.movex * 32)
            self.mapy -= (self.movey * 32)
            return 0
        else:
            return 1

    def A_check(self):
        if(Map.Maping[play_state.round].Npccount>0):
            for Npc in Map.Maping[play_state.round].Npc:
                if self.direct == 0:     # 아래버튼
                    if ( Npc.mapx == self.mapx and Npc.mapy == self.mapy - 32):
                elif self.direct == 1:   # 위버튼
                    if (Npc.mapx == self.mapx and Npc.mapy == self.mapy + 32):
                elif self.direct == 2:   # 왼버튼
                    if (Npc.mapx == self.mapx - 32 and Npc.mapy == self.mapy):
                elif self.direct == 3:   # 오른버튼
                    if (Npc.mapx == self.mapx + 32 and Npc.mapy == self.mapy):



    def Map_move(self,round,mapx,mapy):
        if round == 0:                          # 주인공마을
            if self.mapx // 32 + 1 == 0 :
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 304, 624, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 272, 624, 272
                return 0,0,True,1

            elif self.mapy // 32 + 1 == 13:
                self.mapx, self.mapy, self.chx, self.chy = 368, 16, 368, 16
                return mapx, mapy, True, 6

            elif self.mapy // 32 + 1 == 15:
                self.mapx, self.mapy, self.chx, self.chy = 336, 112, 336, 112
                return mapx, mapy, True, 7

            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 272, 176, 272, 176
                return mapx, mapy, True, 8

            elif self.mapy // 32 + 1 == 5:
                self.mapx, self.mapy, self.chx, self.chy = 272, 176, 272, 176
                return mapx, mapy, True, 9

        elif round == 1:                        # 29번도로
            if self.mapx // 32 + 1 == 61:
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 304, 16, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 272, 16, 272
                return 1280,0,True,0

            elif self.mapx // 32 + 1 == 0:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 816, 336, 624, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 816, 372, 624, 372
                return 0,0, True,2

        elif round == 2:                        # 두번째 마을
            if self.mapy // 32 + 1 == 19:
                if self.mapx // 32 + 1 == 3:
                    self.mapx, self.mapy, self.chx, self.chy = 768, 16, 336, 16
                elif self.mapx // 32 + 1 == 4:
                    self.mapx, self.mapy, self.chx, self.chy = 800, 16, 368, 16
                return 64,0, True,3

            elif self.mapx // 32 + 1 == 27:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 336, 16, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 372, 16, 372
                return mapx,mapy, True,1

            elif self.mapy // 32 + 1 == 9:
                self.mapx, self.mapy, self.chx, self.chy = 272, 16, 272, 16
                return 192, 0, True, 10

            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 272, 16, 272, 16
                return 192, 0, True, 11

            elif self.mapy // 32 + 1 == 11:
                self.mapx, self.mapy, self.chx, self.chy = 272, 16, 272, 16
                return 64, 0, True, 12

            elif self.mapy // 32 + 1 == 15:
                if self.mapx // 32 + 1 == 16:
                    self.mapx, self.mapy, self.chx, self.chy = 272, 16, 272, 16
                    return 192, 0, True, 13
                elif self.mapx // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 304, 16, 304, 16
                    return 64, 0, True, 14

        elif round == 3:                       # 31번 도로
            if self.mapy // 32 + 1 == 0:
                if self.mapx // 32 + 1 == 25:
                    self.mapx, self.mapy, self.chx, self.chy = 64, 560, 16, 560
                if self.mapx // 32 + 1 == 26:
                    self.mapx, self.mapy, self.chx, self.chy = 96, 560, 48, 560
                return 448,0, True,2

            elif self.mapx // 32 + 1 == 0:    # 7,8
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 1248, 336, 624, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 1248, 368, 624, 368
                return 128, 0, True, 4

        elif round == 4:                    # 체육관
            if self.mapx // 32 + 1 == 41:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 128, 336, 16, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 128, 368, 16, 368
                return 640,0, True, 3
            elif self.mapy // 32 + 1 == 11:
                self.mapx, self.mapy, self.chx, self.chy = 272, 16, 272, 16
                return 640,0,True,20
            elif self.mapx // 32 + 1 == 10:
                self.mapx, self.mapy, self.chx, self.chy = 304, 16, 304, 16
                return 128, 160, True, 21
            elif self.mapx // 32 + 1 == 19:
                self.mapx, self.mapy, self.chx, self.chy = 304, 48, 304, 48
                return 160, 160, True, 22
            elif self.mapx // 32 + 1 == 31:
                self.mapx, self.mapy, self.chx, self.chy = 304, 48, 304, 48
                return 640, 160, True, 23
            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 304, 176, 304, 176
                return 640, 128, True, 24
            elif self.mapy // 32 + 1 == 21:
                self.mapx, self.mapy, self.chx, self.chy = 304, 176, 304, 176
                return 64, 192, True, 25

        elif round == 5:                    # 주인공집 2층
            if self.mapy // 32 + 1 == 14:
                self.mapx, self.mapy, self.chx, self.chy = 592, 400, 592, 400
            return mapx, mapy, True, 6

        elif round == 6:                    # 주인공집 1층
            if self.mapy // 32 + 1 == 14:
                self.mapx, self.mapy, self.chx, self.chy = 592, 400, 592, 400
                return mapx, mapy, True, 5

            elif self.mapy // 32 + 1 == 0:
                self.mapx, self.mapy, self.chx, self.chy = 432, 368, 432, 368
                return mapx, mapy, True, 0

        elif round == 7:                    # LAP
            self.mapx, self.mapy, self.chx, self.chy = 208, 432, 208, 432
            return  mapx, mapy, True, 0

        elif round == 8:
            self.mapx, self.mapy, self.chx, self.chy = 112, 176, 112, 176
            return mapx, mapy, True, 0

        elif round == 9:
            self.mapx, self.mapy, self.chx, self.chy = 368, 112, 368, 112
            return mapx, mapy, True, 0

        elif round == 10:
            self.mapx, self.mapy, self.chx, self.chy = 368, 240, 176, 240
            return mapx, mapy, True, 2

        elif round == 11:
            self.mapx, self.mapy, self.chx, self.chy = 560, 176, 368, 176
            return mapx, mapy, True, 2

        elif round == 12:
            self.mapx, self.mapy, self.chx, self.chy = 112, 304, 48, 304
            return mapx, mapy, True, 2
            # 448, 0, 1280, 576

        elif round == 13:
            self.mapx, self.mapy, self.chx, self.chy = 496,432,304,432
            return mapx, mapy, True, 2

        elif round == 14:
            self.mapx, self.mapy, self.chx, self.chy = 304, 432, 240, 432
            return mapx, mapy, True, 2

        elif round == 20:
            self.mapx, self.mapy, self.chx, self.chy = 992, 288, 368, 304
            return mapx, mapy, True, 4
        elif round == 21:
            self.mapx, self.mapy, self.chx, self.chy = 288, 544, 176, 400
            return mapx, mapy, True, 4
        elif round == 22:
            self.mapx, self.mapy, self.chx, self.chy = 576, 544, 432, 400
            return mapx, mapy, True, 4
        elif round == 23:
            self.mapx, self.mapy, self.chx, self.chy = 960, 544, 336, 400
            return mapx, mapy, True, 4
        elif round == 24:
            self.mapx, self.mapy, self.chx, self.chy = 672, 160, 48, 48
            return mapx, mapy, True, 4
        elif round == 25:
            self.mapx, self.mapy, self.chx, self.chy = 96,608,48,432
            return mapx, mapy, True, 4