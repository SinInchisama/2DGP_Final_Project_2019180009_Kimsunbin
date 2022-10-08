from pico2d import *
import Character
import Map

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

                mode = hero.move_check(map_array)  # move_checking.py내 함수 호출
                if mode == 1:
                    Hero_working(direct)
                    mode = 0
                elif mode == 2:
                    round,Map_change = hero.Map_move(round)
                direct = 0
                hero.movex,hero.movey = 0,0



def Hero_working(direct):
    global hero

    for i in range(0,4):
        hero.pngx = 18 + (68 * direct) + 34 * (i % 2)
        print((Maping[round].Nowx > 320 and hero.movex<0),(Maping[round].Nowx < Maping[round].Sizex - 640 and hero.movex>0),Maping[round].Sizex - 640,Maping[round].Nowx)
        if ((Maping[round].Nowx  == 0 and hero.movex<0)or(Maping[round].Nowx == Maping[round].Sizex - 640 and hero.movex>0 )or(Maping[round].Nowx + 640 >= Maping[round].Sizex and Maping[round].Nowx == 0)):
            hero.chx += hero.movex * 8
        else:
            Maping[round].Nowx += hero.movex * 8

        hero.chy += hero.movey * 8


        draw_Scene()
        delay(0.01)

def draw_Scene():       # 전체적인 캔버스에 그리는 함수.
    global round
    global Map_change
    clear_canvas()

    if(Map_change):
        for i in range(15,19):
            Maping[i].map.clip_draw(Maping[i].Nowx, Maping[i].Nowy, 640, 576, 320, 288)
            update_canvas()
            delay(0.05)
            clear_canvas()
        Map_change = False

    Maping[round].map.clip_draw(Maping[round].Nowx, Maping[round].Nowy,640, 576, 320, 288)

    character_image.clip_draw(hero.pngx,hero.pngy,hero.weight,hero.height,hero.chx,hero.chy)

    update_canvas()
    delay(0.05)

open_canvas(640,576)

# init 변수

direct = 0
round = 0
mode = 0
Map_change = False

# Class 변수 생성
hero = Character.Hero(18,3350,32,32,304,304,304,304,0,0)

Maping = [Map.Map(0,0,0,0)for i in range (0,20)] #1 주인공마을 #2 29번도로 #3 첫번째 지나가는 마을 #4 30번도로 #5 체육관 #15~#19 맵이동시를 위한 검은색~흰색

Maping[0].Nowx,Maping[0].Nowy,Maping[0].Sizex,Maping[0].Sizey = 0,0,640,576
Maping[1].Nowx,Maping[1].Nowy,Maping[1].Sizex,Maping[1].Sizey = 1280,0,1920,576
for i in range(15,19):
    Maping[i].Nowx,Maping[i].Nowy,Maping[i].Sizex,Maping[i].Sizey = 0,0,640,576

Maping[0].array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             #1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 4, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [4, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


                   #0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61
Maping[1].array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1, 0, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
                   [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
                   [4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [4, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 3, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 5, 5, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# load_image

character_image = load_image('Character.png')
Maping[0].map = load_image('Main_town1.png')
Maping[1].map = load_image('Route_29_1.png')
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
