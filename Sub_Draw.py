import play_state
from pico2d import *
import Battle

Emergence = None

def Init_SubDraw():
    global Emergence
    Emergence = load_image('./resource/image/emergence.png')


def Emergence(i):
    Emergence = load_image('./resource/image/emergence.png')

    play_state.draw_world()
    Emergence.clip_draw(8 + (i%5)*161,1335 - (i//5)*145,160,144,320,288,640,576)


def Throw_Monster(i):
    Ball = load_image('./resource/image/Ball.png')
    play_state.Maping[19].map.clip_draw(0, 0, 640, 576, 320, 288)  # 흰배경
    play_state.hero.pList[Battle.Poket_Order].Back_Draw(120, 240, 48, 47, 224, 224)  # 내 포켓몬 그리기
    if(i<40):
        Ball.clip_composite_draw(0,0,16,16,(i-40)*15,'',500,450+(4*(i-40)),32,32)
    else:
        Ball.clip_composite_draw(0, 0, 16, 16, (i - 40) * 15, '', 500, 490 - (3 * (i - 40)), 32, 32)
