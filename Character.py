class character:
    def __init__(self,pngx,pngy,height,weight,mapx,mapy):       # battle npc,hero, give Npc 상속 위한 기본 클래스
        self.pngx = pngx
        self.pngy = pngy
        self.height = height
        self.weight = weight
        self.mapx = mapx
        self.mapy = mapy

class Hero(character):
    def __init__(self,pngx,pngy,height,weight,chx,chy,mapx,mapy):       # 이후 추가 예정
        character.__init__(self,pngx,pngy,height,weight,mapx,mapy)
        self.chx = chx
        self.chy = chy

    def move_check(self,map_array,chdirect):               # 후에 여기에 round 매개변수 추가해서 4에 접근할때나 포켓몬 나오는거 조정예정
        if chdirect == 1:                                  # 왼쪽 방향으로 이동
            self.mapx -= 16
            if (map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 1 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 5): # 보드칸 크기가 16 x 16
                print(self.mapx, self.mapy,self.mapy)
                return 1
            elif (map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 4):
                self.chx -= 16
                pass
            elif (map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 0 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 2 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 3):
                self.mapx += 16
        elif chdirect == 2:
            self.mapx +=16
            if (map_array[self.mapy // 16][self.mapx // 16 + 1] == 1 or map_array[self.mapy // 16][self.mapx // 16 + 1] == 5):  # 보드칸 크기가 16 x 16
                print(self.mapx, self.mapy)
                self.chx += 16
                return 1
            elif (map_array[self.mapy // 16][self.mapx // 16 + 1] == 4):
                self.chx += 16
                pass
            elif (map_array[self.mapy // 16][self.mapx // 16 + 1] == 0 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 2 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 3):
                self.mapx -= 16
        elif chdirect == 3:
            self.mapy += 16
            if (map_array[self.mapy // 16+ 1][self.mapx // 16 + 1] == 1 or map_array[self.mapy // 16+ 1][self.mapx // 16 + 1] == 5):  # 보드칸 크기가 16 x 16
                self.chy += 16
                return 1
                print(self.mapx, self.mapy)
            elif (map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 4):
                self.chy += 16
                pass
            elif (map_array[self.mapy // 16+ 1][self.mapx // 16 + 1] == 0 or map_array[self.mapy // 16+ 1][self.mapx // 16 + 1] == 2 or map_array[self.mapy // 16 + 1][self.mapx // 16 + 1] == 3):
                self.mapy -= 16
        print(map_array[self.mapy // 16 + 1][(self.mapx) // 16 + 1])
        print((self.mapx)//16 + 1,(self.mapy)//16 + 1)
        return 0
