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

    def Map_move(self,round):
        if round == 0:
            if self.mapx // 32 + 1 == 0 :
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 304, 624, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 1904, 272, 624, 272
                return 1,1
        if round == 1:
            if self.mapx // 32 + 1 == 61:
                if self.mapy // 32 + 1 == 10:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 304, 16, 304
                elif self.mapy // 32 + 1 == 9:
                    self.mapx, self.mapy, self.chx, self.chy = 0, 272, 16, 272
                return 0,True
            if self.mapx // 32 + 1 == 0:
                if self.mapy // 32 + 1 == 11:
                    self.mapx, self.mapy, self.chx, self.chy = 816,336,16,336
                elif self.mapy // 32 + 1 == 12:
                    self.mapx, self.mapy, self.chx, self.chy = 816, 372, 16, 372
                    return 2, True