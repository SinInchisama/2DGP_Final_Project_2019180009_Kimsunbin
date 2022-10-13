import Character
from Map import Maping
from Map import init_map


Maping[6].Npccount = 1
Maping[6].Npc = [Character.character(51, 3111, 32, 32, 304, 240) for i in range(0, 1)]  # 어무니

Maping[7].Npccount = 3
Maping[7].Npc = [Character.character(52, 3213, 32, 32, 304, 400) for i in range(0, 1)]  #박사님
Maping[7].Npc.append(Character.character(290, 3044, 32, 32, 272, 112))                   #조교
Maping[7].Npc.append(Character.character(222, 3044, 32, 32, 464, 208))                   #조교

Maping[8].Npccount = 1
Maping[8].Npc = [Character.character(154, 2635, 32, 32, 432, 336) for i in range(0, 1)]  #할아버지

Maping[9].Npccount = 1
Maping[9].Npc = [Character.character(289, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지
Maping[9].Npc.append(Character.character(222, 2566, 32, 32, 368, 304))

Maping[10].Npc = [Character.character(224, 3146, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지

Maping[11].Npc = [Character.character(154, 3077, 32, 32, 272, 304) for i in range(0, 1)]  #할아버지

Maping[12].Npc = [Character.character(224, 3146, 32, 32, 336, 336) for i in range(0, 1)]  #할아버지




