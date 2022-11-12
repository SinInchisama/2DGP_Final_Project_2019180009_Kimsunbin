from pico2d import *
import game_framework
import Professor_state
class Map:
    def __init__(self,Sizex,Sizey,startx,starty,endx,endy,nowx,nowy):
        self.Sizex = Sizex
        self.Sizey = Sizey
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.nowx = nowx
        self.nowy = nowy

Background_image = Map(320,288,16,2033,0,687,16,2033)
image1 = None
frame = None

# 16 1743 2079
def enter():
    global Background_image,image1,frame
    image1 = load_image('./resource/image/3.png')
    Background_image.image = load_image('./resource/image/title_state.png')
    image1.clip_draw(0, 0, 640, 576, 320, 288)
    frame = 0
    print('fdf')
    Background_image.image.clip_draw(Background_image.nowx, Background_image.nowy, 320, 288, 320,288)
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                game_framework.change_state(Professor_state)

def update():
    global frame
    frame = (frame + 0.2) % 5
    # Background_image.nowy -= 336
    # if Background_image.nowy <= Background_image.endy:
    #     Background_image.nowy = Background_image.starty
    pass

def draw():
    global frame
    clear_canvas()
    image1.clip_draw(0, 0, 640, 576, 320, 288)
    Background_image.image.clip_draw(Background_image.nowx, Background_image.nowy - (336 * int(frame)), 320, 288, 320, 288,640,576)
    update_canvas()
    delay(0.02)
    pass

def exit():
    pass