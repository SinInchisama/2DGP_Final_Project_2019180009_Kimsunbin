from pico2d import *
import play_state
import game_framework

image = None
set_Ball,Ball_count,Frame = None,None,None

def enter():
    global image,set_Ball,Ball_count,Frame
    Ball_count = 0
    set_Ball = False
    Frame = 0
    image = load_image('./resource/image/Ball.png')
    pass
def exit():
    for i in play_state.hero.pList:
        i.Hp = i.MaxHp
        i.ailment = None
    pass
def draw():
    global Ball_count,Frame
    clear_canvas()

    play_state.draw_world()
    for i in range(0,int(Ball_count)):
        image.clip_draw(16 * (int(Frame)%2),0,16,16,26 + 14*(i%2),486 - 10*(i//2),12,12)

    update_canvas()
    delay(0.03)
    pass
def resume():
    pass
def pause():
    pass
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def update():
    global Ball_count,Frame,set_Ball
    if(not(set_Ball)):
        if(Ball_count<len(play_state.hero.pList)):
            Ball_count += 0.1
        else:
            set_Ball = True
    else:
        Frame += 0.1
        if(Frame >= 10.0):
            game_framework.pop_state()
    pass