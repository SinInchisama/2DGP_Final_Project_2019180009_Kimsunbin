import Character
from Map import Maping

class Npc(Character.character):
    def __init__(self,pngx,pngy,height,weight,mapx,mapy):
        Character.character.__init__(self,pngx,pngy,height,weight,mapx,mapy)


Maping[1].Npccount = 1
Maping[1].Npc = [Npc(154, 2261, 32, 32, 336, 208) for i in range(0, 1)]  # 어무니


Maping[3].Npccount = 1
Maping[3].Npc = [Npc(154, 2261, 32, 32, 528, 80) for i in range(0, 1)]  # 어무니
Maping[3].Npc.append(Npc(290, 3044, 32, 32, 560, 240))

Maping[6].Npccount = 1
Maping[6].Npc = [Npc(51, 3111, 32, 32, 304, 240) for i in range(0, 1)]  # 어무니


Maping[7].Npccount = 3
Maping[7].Npc = [Npc(52, 3213, 32, 32, 304, 400) for i in range(0, 1)]  #박사님
Maping[7].Npc.append(Npc(290, 3044, 32, 32, 272, 112))                   #조교
Maping[7].Npc.append(Npc(222, 3044, 32, 32, 464, 208))                   #조교

Maping[8].Npccount = 1
Maping[8].Npc = [Npc(154, 2635, 32, 32, 432, 336) for i in range(0, 1)]  #할아버지

Maping[9].Npccount = 1
Maping[9].Npc = [Npc(289, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지
Maping[9].Npc.append(Npc(222, 2566, 32, 32, 368, 304))

Maping[10].Npccount = 1
Maping[10].Npc = [Npc(224, 3146, 32, 32, -50, -50) for i in range(0, 1)]  #할아버지

Maping[11].Npccount = 1
Maping[11].Npc = [Npc(154, 3077, 32, 32, 336, 336) for i in range(0, 1)]  #할아버지

Maping[12].Npccount = 1
Maping[12].Npc = [Npc(289, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지

Maping[13].Npccount = 1
Maping[13].Npc = [Npc(18, 2908, 32, 32, 272, 368) for i in range(0, 1)]  #마트판매원

Maping[14].Npccount = 1
Maping[14].Npc = [Npc(290, 2839, 32, 32, 176, 304) for i in range(0, 1)]  #간호순

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





