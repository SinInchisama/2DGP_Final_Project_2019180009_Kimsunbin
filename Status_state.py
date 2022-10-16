from pico2d import *
import game_framework
import play_state
import Poketmon

Status_iamge = None
image3 = None
select = None

def enter():
    global Status_iamge,image3,select
    Status_iamge = [load_image('./resource/image/Status_state.png')]
    Status_iamge.append(load_image('./resource/image/Skill_state.png'))
    Status_iamge.append(load_image('./resource/image/ability_state.png'))
    image3 = load_image('All_Pokemon.png')
    select = 0
    pass

def handle_events():
    global select
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if(select - 1 >= 0):
                    select -= 1
            elif event.key == SDLK_RIGHT:
                select = (select + 1) % 3

            elif event.key == SDLK_UP:
                play_state.hero.pList[0].Num += 1

            elif event.key == SDLK_DOWN:
                play_state.hero.pList[0].Num -= 1


def update():
    pass

def draw():
    clear_canvas()
    Status_iamge[select].clip_draw(0,0,160,144,320,288,640,576)
    image3.clip_draw(Poketmon.Poket_Data[play_state.hero.pList[0].Num].Pngx, Poketmon.Poket_Data[play_state.hero.pList[0].Num].Pngy, 56, 56, 120, 450, 224, 224)
    update_canvas()
    pass