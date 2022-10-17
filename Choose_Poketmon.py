from pico2d import *
import game_framework
import Status_state
import play_state
import Poketmon

Choose_image = None
Cursor_image = None
CusorY = None
frame = None
Pframe = None

def enter():
    global Menu_image,CusorY,Cursor_image,frame,Pframe
    Menu_image = load_image('./resource/image/Choose_Poketmon.png')
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    frame = 0
    Pframe = 0
    pass

def handle_events():
    global CusorY,frame
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.pop_state()
            elif event.key == SDLK_DOWN:
                if CusorY + 1 < play_state.hero.Pcount:
                    CusorY = (CusorY + 1) % 7
                else:
                    CusorY = 6
                print (CusorY)
            elif event.key == SDLK_UP:
                if(CusorY >0):
                    CusorY-= 1
            elif event.key == SDLK_a:
                if (CusorY != 6):
                    game_framework.push_state(Status_state)
                    # frame = 645       # 포켓몬 선택하고 무슨 행동할지 선택하는 창
                elif(CusorY == 6):
                    game_framework.pop_state()
def draw():
    clear_canvas()
    Menu_image.clip_draw(5 + frame, 7, 640, 576, 320, 288)
    Cursor_image.clip_draw(0, 0, 32, 32, 15, 525 - (64 * CusorY))           # 커서 위치

    for i in range(0,play_state.hero.Pcount):           # player가 가진 포켓몬 숫자만큼 출력
        play_state.hero.character_image.clip_draw(220 + (int(Pframe) * 34),610,36,36,45,525- (64 * i))      # 포켓몬 이미지

        Acount = 0

        for Alpha in Poketmon.Poket_Data[play_state.hero.pList[i].Num].name:        # 포켓몬 이름 출력
            play_state.Font_image.clip_draw(167 +((ord(Alpha) - 97) % 16) * 9,437 - ((ord(Alpha) - 97) // 16) * 9,8,8,80 + (Acount * 16),520- (64 * i),16,16)
            Acount += 1

        play_state.Font_image.clip_draw(275, 446, 8, 8, 260, 520 - (64 * i), 16, 16)        # :
        play_state.Font_image.clip_draw(266, 455, 8, 8, 280, 520 - (64 * i), 16, 16)        # L

        Acount,div = 0,1
        while play_state.hero.pList[i].level // div != 0:
            result = (play_state.hero.pList[i].level // div) % 10
            play_state.Font_image.clip_draw(221 + result * 9, 392, 8, 8, 340 - (Acount * 16), 520 - (64 * i), 16, 16)
            Acount += 1
            div *= 10

        Acount, div = 0, 1
        while play_state.hero.pList[i].MaxHp // div != 0:
            result = (play_state.hero.pList[i].MaxHp // div) % 10
            play_state.Font_image.clip_draw(221 + result * 9, 392, 8, 8, 480 - (Acount * 16), 540 - (64 * i), 16, 16)
            Acount += 1
            div *= 10

        Acount, div = 0, 1
        while play_state.hero.pList[i].Hp // div != 0:
            result = (play_state.hero.pList[i].Hp // div) % 10
            play_state.Font_image.clip_draw(221 + result * 9, 392, 8, 8, 550 - (Acount * 16), 540 - (64 * i), 16, 16)
            Acount += 1
            div *= 10

        play_state.Font_image.clip_draw(194, 392, 8, 8, 500, 540 - (64 * i), 16, 16)

    update_canvas()
    pass

def update():
    global Pframe
    Pframe = (Pframe + 0.01) % 2
    pass

def exit():
    pass

def pause():
    pass

def resume():
    pass