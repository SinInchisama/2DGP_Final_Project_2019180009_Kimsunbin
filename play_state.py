from pico2d import *
import Character
from Map import Maping
from Map import init_map
from Map import Draw_Map
import game_framework
import Menu_state
import Poketmon
import random
import wild_Battle
import Skill_Data
import PokeDex


round,mode,running,Map_change =0,0,None,None
Font_image,Font_Color,HPbar_image,Hp_image,Board,Pokedex,state = None,None,None,None,None,None,None
Back_Music,Battle_Music = None,None
hero = None

def enter():
    global round,mode,running,Map_change,hero,Font_image,HPbar_image,Hp_image,Board,Pokedex,Font_Color,Back_Music,Battle_Music
    Battle_Music = load_music('./resource/music/Battle_Music.mp3')
    Battle_Music.set_volume(10)
    Back_Music = load_music('./resource/music/Background.mp3')
    Back_Music.set_volume(10)
    Back_Music.repeat_play()
    round = 5  # 맵 변경에 사용하는 변수
    mode = 0  # 각종 모드에 사용하는 변수
    running = True
    Map_change = False  # 맵변경시 깜빡이는 효과를 내기 위한 변수
    init_map()
    hero = Character.Hero(18,3350,32,32,304,304,304,304,0,0)
    # hero = Character.Hero(18,3350,32,32,624, 368, 1248, 352,0,0)
    hero.character_image = pico2d.load_image('./resource/image/Character.png')
    Font_image = pico2d.load_image('./resource/image/Font.png')
    Font_Color = pico2d.load_image('./resource/image/Font_Color.png')
    HPbar_image = pico2d.load_image('./resource/image/Hp_bar.png')
    Hp_image = pico2d.load_image('./resource/image/Hp.png')
    Board = pico2d.load_image('./resource/image/Board.png')
    Poketmon.init_Poketmon()
    Poketmon.init_Skill()
    Skill_Data.init_skill()
    Pokedex = PokeDex.PokeDex()


def handle_events():
    global hero
    global mode
    global round
    events = get_events()
    for event in events:

        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:  # 왼쪽 버튼 눌리면
                if(not(hero.Movecheck)):
                    hero.direct = 2  # array가 1 또는 5면 ch값 -16)
                    hero.movex -= 1
                    hero.Movecheck = True
            elif event.key == SDLK_RIGHT:
                if (not (hero.Movecheck)):
                    hero.direct = 3  # 오른쪽 버튼 눌리면
                    hero.movex += 1
                    hero.Movecheck = True
            elif event.key == SDLK_UP:  # 윗 버튼 눌리면
                if (not (hero.Movecheck)):
                    hero.direct = 1
                    hero.movey += 1
                    hero.Movecheck = True

            elif event.key == SDLK_DOWN:  # 아래 버튼 눌리면
                if (not (hero.Movecheck)):
                    hero.direct = 0
                    hero.movey -= 1
                    hero.Movecheck = True

            elif event.key == SDLK_x:  # 윗 버튼 눌리면
                hero.Can_riding()
            elif event.key == SDLK_a:
                hero.A_check()

            elif event.key == SDLK_c:
                game_framework.push_state(Menu_state)

            elif event.key == SDLK_h:
                for i in hero.pList:
                    i.Hp = i.MaxHp
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:  # 왼쪽 버튼 눌리면
                hero.movex = 0

                hero.Movecheck = False
            elif event.key == SDLK_RIGHT:
                hero.movex = 0

                hero.Movecheck = False
            elif event.key == SDLK_UP:  # 윗 버튼 눌리면
                hero.movey = 0
                hero.Movecheck = False
            elif event.key == SDLK_DOWN:  # 윗 버튼 눌리면
                hero.movey = 0
                hero.Movecheck = False
def Hero_working(mode):
    global hero,state


    if(hero.Movecheck):
        for i in range(0,4):
            hero.pngx = 18 + (68 * hero.direct) + 34 * (i % 2)
        # if ((Maping[round].Nowx  == 0 and hero.movex<0)or(Maping[round].Nowx == Maping[round].Sizex - 640 and hero.movex>0 )or(Maping[round].Nowx + 640 >= Maping[round].Sizex and Maping[round].Nowx == 0)):
        # 캐릭터가 왼쪽벽에 부딪히거나 오른쪽벽에 부딪힐때, 그리고 맵크기가 weight가 640보다 클 때 맵이 움직임.
            if ((hero.chx == 48 and hero.movex<0 and Maping[round].Nowx != 0) or(hero.chx == 592 and hero.movex>0 and Maping[round].Nowx != Maping[round].Sizex - 640) ):
                Maping[round].Minusx += hero.movex * 8
            elif(hero.movex != 0):
                hero.chx += hero.movex * 8
            elif ((hero.chy == 48 and hero.movey < 0 and Maping[round].Nowy != 0) or (hero.chy == 528 and hero.movey > 0 and Maping[round].Nowy != Maping[round].Sizey - 576)):
                Maping[round].Minusy += hero.movey * 8
            elif(hero.movey !=0 ):
                hero.chy += hero.movey * 8
            draw()
            delay(hero.Speed)
        if(Maping[round].Minusx == 32 or Maping[round].Minusx == -32):
            Maping[round].Nowx += hero.movex * 32
            Maping[round].Minusx = 0
        elif(Maping[round].Minusy == 32 or Maping[round].Minusy == -32):
            Maping[round].Nowy += hero.movey * 32
            Maping[round].Minusy = 0
        if(mode == 3):
            if(not(hero.step)):
                if(random.randint(0,100)<20):
                    wild_Battle.Battle_type = 'Wild'
                    game_framework.push_state(wild_Battle)
                    hero.movey = 0
                    hero.movex = 0
                    hero.Movecheck = False

        # print(hero.mapx, hero.mapy, hero.chx, hero.chy,Maping[round].Nowx, Maping[round].Nowy,hero.movex, hero.movey,)


def draw():       # 전체적인 캔버스에 그리는 함수.
    global round
    global Map_change
    clear_canvas()

    if(Map_change):             # 맵 변경시 깜빡이는 이미지 출력
        for i in range(15,19):
            Maping[i].map.clip_draw(Maping[i].Nowx, Maping[i].Nowy, 640, 576, 320, 288)
            update_canvas()
            delay(0.03)
            clear_canvas()
        Map_change = False
        hero.Movecheck,hero.movex,hero.movey  = False, 0, 0

    draw_world()
    update_canvas()
    delay(0.001)

def draw_world():
    Draw_Map(round)

    if Maping[round].Npccount != 0:
        for Npc in Maping[round].Npc:
            hero.character_image.clip_draw(Npc.pngx, Npc.pngy, Npc.weight, Npc.height, Npc.mapx - Maping[round].Nowx - Maping[round].Minusx,
                                           Npc.mapy - - Maping[round].Nowy - Maping[round].Minusy)

    hero.character_image.clip_draw(hero.pngx, hero.pngy, hero.weight, hero.height, hero.chx, hero.chy)

def update():
    global mode
    global Maping,Map_change,round
    if hero.Movecheck:
        mode = hero.move_check(Maping[round].array)  # move_checking.py내 함수 호출, 맵 행렬이 갈 수 있는지 체크하는 클래스함수
        # print(Maping[round].Nowx,Maping[round].Nowy)
        if mode == 1 or mode == 3:
            Hero_working(mode)  # 걷는 애니매이션 출력
            mode = 0
        elif mode == 2:
            Hero_working(mode)
            Maping[round].Nowx, Maping[round].Nowy, Map_change, round = hero.Map_move(round, Maping[round].Nowx, Maping[round].Nowy)  # 행렬이 4일때 맵변경을 위한 함수
def pause():
    pass

def resume():
    pass