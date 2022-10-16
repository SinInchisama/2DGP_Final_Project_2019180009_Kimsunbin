from pico2d import *
import game_framework
import title_state
import Poketmon

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


Background_image = [Map(320,288,17,304,1360,0,17,3058) for i in range(0,2)]
image1 = None
order = None

def enter():
    global Background_image,order,image1,image3
    image1 = load_image('./resource/image/3.png')
    Background_image[0].image = load_image('./resource/image/logo.imgae_01.png')
    Background_image[1].image = load_image('./resource/image/logo.imgae_02.png')
    Background_image[1].nowy = 4274
    Background_image[1].endy = 600
    order = 0
    image1.clip_draw(0, 0, 640, 576, 320, 288)
    Background_image[order].image.clip_draw(Background_image[order].nowx, Background_image[order].nowy, 320, 288, 320,288)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                game_framework.change_state(title_state)
    pass

#(Npc.pngx,Npc.pngy,Npc.weight,Npc.height,Npc.mapx - Maping[round].Nowx,Npc.mapy - - Maping[round].Nowy)
def update():
    global order
    Background_image[order].nowx += 336
    if(Background_image[order].nowx >= Background_image[order].endx):
        Background_image[order].nowx = Background_image[order].startx
        Background_image[order].nowy -= 304
        if Background_image[order].nowy <= Background_image[order].endy:
            if(order == 0):
                order += 1
            else:
                game_framework.change_state(title_state)
    pass

def draw():
    clear_canvas()
    image1.clip_draw(0, 0, 640, 576, 320, 288)
    Background_image[order].image.clip_draw(Background_image[order].nowx,Background_image[order].nowy,320,288,320,288)
    # image3.clip_draw(Poketmon.Poket_Data[2].Pngx, Poketmon.Poket_Data[2].Pngy, 56, 56, 320, 288, 224, 224)
    update_canvas()
    delay(0.05)
    pass

def exit():
    pass
