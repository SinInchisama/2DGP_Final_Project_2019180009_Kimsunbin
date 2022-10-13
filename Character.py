import pico2d

class character:
    def __init__(self,pngx,pngy,height,weight,mapx,mapy):       # battle npc,hero, give Npc 상속 위한 기본 클래스
        self.pngx = pngx
        self.pngy = pngy
        self.height = height
        self.weight = weight
        self.mapx = mapx
        self.mapy = mapy

class Hero(character):
    def __init__(self,pngx,pngy,height,weight,chx,chy,mapx,mapy,movex,movey):       # 이후 추가 예정
        character.__init__(self,pngx,pngy,height,weight,mapx,mapy)
        self.chx = chx
        self.chy = chy
        self.movex = movex
        self.movey = movey

    def move_check(self,map_array):               # 후에 여기에 round 매개변수 추가해서 4에 접근할때나 포켓몬 나오는거 조정예정
        self.mapx += (self.movex * 32)
        self.mapy += (self.movey * 32)
        print(self.movex,self.movey,self.mapx,self.mapy,self.chx,self.chy)
        if (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 1 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 5):
            return 1
        elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 4):
            return 2
        elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 0 or map_array[self.mapy // 32 + 1][ self.mapx // 32 + 1] == 2 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 3):
            self.mapx -= (self.movex * 32)
            self.mapy -= (self.movey * 32)
            return 0

    def Map_move(self,round,mapx,mapy):
        if round == 0:                          # 주인공마을
            if self.mapx // 32 + 1 == 0 :
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 304, 624, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 272, 624, 272
                return mapx,mapy,True,1

            elif self.mapy // 32 + 1 == 13:
                self.mapx, self.mapy, self.chx, self.chy = 352, 192, 368, 176
                return mapx, mapy, True, 6

            elif self.mapy // 32 + 1 == 15:
                self.mapx, self.mapy, self.chx, self.chy = 320, 128, 336, 112
                return mapx, mapy, True, 7

            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return mapx, mapy, True, 8

            elif self.mapy // 32 + 1 == 5:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return mapx, mapy, True, 9

        elif round == 1:                        # 29번도로
            if self.mapx // 32 + 1 == 61:
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 304, 16, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 272, 16, 272
                return mapx,mapy,True,0

            elif self.mapx // 32 + 1 == 0:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 816, 336, 624, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 816, 372, 624, 372
                return mapx,mapy, True,2

        elif round == 2:                        # 두번째 마을
            if self.mapy // 32 + 1 == 19:
                if self.mapx // 32 + 1 == 3:
                    self.mapx, self.mapy, self.chx, self.chy = 768, 0, 336, 16
                elif self.mapx // 32 + 1 == 4:
                    self.mapx, self.mapy, self.chx, self.chy = 800, 0, 368, 16
                return 64,0, True,3

            elif self.mapx // 32 + 1 == 27:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 336, 16, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 372, 16, 372
                return mapx,mapy, True,1

            elif self.mapy // 32 + 1 == 9:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return 192, 0, True, 10

            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return 192, 0, True, 11

            elif self.mapy // 32 + 1 == 11:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return 64, 0, True, 12

            elif self.mapy // 32 + 1 == 15:
                if self.mapx // 32 + 1 == 16:
                    self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                    return 192, 0, True, 13
                elif self.mapx // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 256, 192, 240, 176
                    return 64, 0, True, 14

        elif round == 3:                       # 31번 도로
            if self.mapy // 32 + 1 == 0:
                if self.mapx // 32 + 1 == 25:
                    self.mapx, self.mapy, self.chx, self.chy = 64, 576, 16, 560
                if self.mapx // 32 + 1 == 26:
                    self.mapx, self.mapy, self.chx, self.chy = 64, 576, 48, 560
                return 448,0, True,2

            elif self.mapx // 32 + 1 == 4:    # 7,8
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 1248, 320, 624, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 1248, 352, 624, 368
                return mapx, mapy, True, 4

        elif round == 4:                    # 체육관
            if self.mapx // 32 + 1 == 41:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 128, 320, 16, 336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 128, 352, 16, 368
                return 640,0, True, 3
            elif self.mapy // 32 + 1 == 11:
                self.mapx, self.mapy, self.chx, self.chy = 288, 192, 272, 176
                return 640,0,True,20
            elif self.mapx // 32 + 1 == 10:
                self.mapx, self.mapy, self.chx, self.chy = 256, 192, 240, 176
                return 128, 160, True, 21
            elif self.mapx // 32 + 1 == 19:
                self.mapx, self.mapy, self.chx, self.chy = 320, 64, 304, 48
                return 160, 160, True, 22
            elif self.mapx // 32 + 1 == 31:
                self.mapx, self.mapy, self.chx, self.chy = 320, 64, 304, 48
                return 640, 160, True, 23
            elif self.mapy // 32 + 1 == 7:
                self.mapx, self.mapy, self.chx, self.chy = 320, 192, 304, 176
                return 640, 128, True, 24
            elif self.mapy // 32 + 1 == 21:
                self.mapx, self.mapy, self.chx, self.chy = 320, 192, 304, 176
                return 64, 192, True, 25
        elif round == 5:                    # 주인공집 2층
            if self.mapy // 32 + 1 == 12:
                self.mapx, self.mapy, self.chx, self.chy = 448, 384, 464, 368
            return mapx, mapy, True, 6

        elif round == 6:                    # 주인공집 1층
            if self.mapy // 32 + 1 == 14:
                self.mapx, self.mapy, self.chx, self.chy = 432, 336, 432, 336
                return mapx, mapy, True, 5

            elif self.mapy // 32 + 1 == 6:
                self.mapx, self.mapy, self.chx, self.chy = 432, 368, 432, 368
                return mapx, mapy, True, 0

        elif round == 7:                    # LAP
            if self.mapy // 32 + 1 == 4:
                self.mapx, self.mapy, self.chx, self.chy = 208, 432, 208, 432
                return  mapx, mapy, True, 0

        elif round == 8:
            if self.mapy // 32 + 1 == 6:
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