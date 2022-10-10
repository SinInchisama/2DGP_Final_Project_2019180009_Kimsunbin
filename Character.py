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

        if (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 1 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 5):
            return 1
        elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 4):
            return 2
        elif (map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 0 or map_array[self.mapy // 32 + 1][ self.mapx // 32 + 1] == 2 or map_array[self.mapy // 32 + 1][self.mapx // 32 + 1] == 3):
            self.mapx -= (self.movex * 32)
            self.mapy -= (self.movey * 32)
            return 0

    def Map_move(self,round,mapx,mapy):
        if round == 0:
            if self.mapx // 32 + 1 == 0 :
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 304, 624, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 272, 624, 272
                return mapx,mapy,1,1
        elif round == 1:
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
        elif round == 2:
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
        elif round == 3:
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
            # 448, 0, 1280, 576