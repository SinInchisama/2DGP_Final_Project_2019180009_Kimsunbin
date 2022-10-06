from pico2d import *
import Character

direct = 0
round = 0
hero = Character.Hero(9,1675,16,16,152,152,152,152)
mode = 0

def handle_events(map_array):
    global direct
    global hero
    global mode
    events = get_events()
    for event in events:


        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:                           # 왼쪽 버튼 눌리면
                direct = 1                                       # array가 1 또는 5면 ch값 -16)
            elif event.key == SDLK_RIGHT:
                direct = 2# 오른쪽 버튼 눌리면

            elif event.key == SDLK_UP:                          # 윗 버튼 눌리면
                direct = 3

            print(direct,hero.chx,hero.mapx)
            mode = hero.move_check(map_array, direct)  # move_checking.py내 함수 호출
            print(mode,hero.chx,hero.mapx)
            if mode == 1:
                Hero_working(direct)
                mode = 0
            direct = 0



def Hero_working(direct):
    global hero
    if direct == 1:
        for i in range(0,2,1):
            hero.pngx = 105 + 16 * (i%2)
            hero.chx -= 8
            draw_Scene()
            delay(0.1)



# def move_check(map_array,chdirect):
#     global hero
#     if chdirect == 1:
#         hero.chx -= 16
#         if (map_array[hero.chy // 16][hero.chx // 16+1] == 1 or map_array[hero.chy // 16][hero.chx // 16+1] == 5):
#             # 보드칸 크기가 16 x 16
#             print(hero.chx, hero.chy)
#         elif (map_array[hero.chy // 16][hero.chx // 16 + 1] == 4):
#             hero.chx += 32
#             pass
#         print(map_array[hero.chy // 16][(hero.chx - 16) // 16])
#         print((hero.chx-16)//16,(hero.chy-16)//16)



def draw_Scene():       # 전체적인 캔버스에 그리는 함수.
    global round
    clear_canvas()
    if (round == 0):
        main_town_map.clip_draw(0, 0, 320, 288, 160, 144)
    elif(round==1):
        pass
    character_image.clip_draw(hero.pngx,hero.pngy,hero.weight,hero.height,hero.chx,hero.chy)

    update_canvas()

open_canvas(320,288)

main_map_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
             [4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

map = load_image('First_gym.png')
main_town_map = load_image('Main_town1.png')
character_image = load_image('Character.png')

while True:
    draw_Scene()
    handle_events(main_map_array)
    delay(0.001)
    get_events()



close_canvas()
