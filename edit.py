from pico2d import *
import Character
from Map import Maping

def handle_events(map_array):
    global direct
    global hero
    global mode
    global round
    global Map_change
    events = get_events()
    for event in events:


        if event.type == SDL_KEYDOWN:
            if direct == 0:
                if event.key == SDLK_LEFT:                           # 왼쪽 버튼 눌리면
                    direct = 2                                       # array가 1 또는 5면 ch값 -16)
                    hero.movex -= 1
                elif event.key == SDLK_RIGHT:
                    direct = 3# 오른쪽 버튼 눌리면
                    hero.movex += 1

                elif event.key == SDLK_UP:                          # 윗 버튼 눌리면
                    direct = 1
                    hero.movey += 1

                elif event.key == SDLK_DOWN:  # 윗 버튼 눌리면
                    direct = 0
                    hero.movey -= 1

                mode = hero.move_check(map_array)  # move_checking.py내 함수 호출, 맵 행렬이 갈 수 있는지 체크하는 클래스함수
                if mode == 1:
                    Hero_working(direct)            # 걷는 애니매이션 출력
                    mode = 0
                elif mode == 2:
                    Maping[round].Nowx,Maping[round].Nowy,Map_change,round = hero.Map_move(round,Maping[round].Nowx,Maping[round].Nowy)     # 행렬이 4일때 맵변경을 위한 함수
                direct = 0
                hero.movex,hero.movey = 0,0



def Hero_working(direct):
    global hero

    for i in range(0,4):
        hero.pngx = 18 + (68 * direct) + 34 * (i % 2)
        # if ((Maping[round].Nowx  == 0 and hero.movex<0)or(Maping[round].Nowx == Maping[round].Sizex - 640 and hero.movex>0 )or(Maping[round].Nowx + 640 >= Maping[round].Sizex and Maping[round].Nowx == 0)):
        # 캐릭터가 왼쪽벽에 부딪히거나 오른쪽벽에 부딪힐때, 그리고 맵크기가 weight가 640보다 클 때 맵이 움직임.
        if ((hero.chx == 16 and hero.movex<0 and Maping[round].Nowx != 0) or(hero.chx == 624 and hero.movex>0 and Maping[round].Nowx != Maping[round].Sizex - 640) ):
            Maping[round].Nowx += hero.movex * 8
        elif(hero.movex != 0):
            hero.chx += hero.movex * 8
        elif ((hero.chy == 16 and hero.movey < 0 and Maping[round].Nowy != 0) or (hero.chy == 560 and hero.movey > 0 and Maping[round].Nowy != Maping[round].Sizey - 576)):
            Maping[round].Nowy += hero.movey * 8
        elif(hero.movey !=0):
            hero.chy += hero.movey * 8


        draw_Scene()
        delay(0.001)

def draw_Scene():       # 전체적인 캔버스에 그리는 함수.
    global round
    global Map_change
    clear_canvas()

    if(Map_change):             # 맵 변경시 깜빡이는 이미지 출력
        for i in range(15,19):
            Maping[i].map.clip_draw(Maping[i].Nowx, Maping[i].Nowy, 640, 576, 320, 288)
            update_canvas()
            delay(0.05)
            clear_canvas()
        Map_change = False

    Maping[round].map.clip_draw(Maping[round].Nowx, Maping[round].Nowy,640, 576, 320, 288)

    character_image.clip_draw(hero.pngx,hero.pngy,hero.weight,hero.height,hero.chx,hero.chy)

    update_canvas()
    delay(0.001)

open_canvas(640,576)

# init 변수

direct = 0      # 방향
round = 0       # 맵 변경에 사용하는 변수
mode = 0        # 각종 모드에 사용하는 변수
Map_change = False  # 맵변경시 깜빡이는 효과를 내기 위한 변수

# Class 변수 생성
hero = Character.Hero(18,3350,32,32,304,304,304,304,0,0) #,pngx,pngy,height,weight,chx,chy,mapx,mapy,movex,movey):
# hero = Character.Hero(18,3350,32,32,624, 368,1248, 352,0,0)

# load_image

character_image = load_image('Character.png')
Maping[0].map = load_image('Main_town1.png')
Maping[1].map = load_image('Route_29_1.png')
Maping[2].map = load_image('Second_town.png')
Maping[3].map = load_image('Route_31_1.png')
Maping[4].map = load_image('First_gym_1.png')
Maping[15].map = load_image('2.png')
Maping[16].map = load_image('3.png')
Maping[17].map = load_image('4.png')
Maping[18].map = load_image('5.png')
Maping[19].map = load_image('1.png')


while True:
    draw_Scene()
    handle_events(Maping[round].array)
    delay(0.001)





close_canvas()
