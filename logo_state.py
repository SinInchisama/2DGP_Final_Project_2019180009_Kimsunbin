from pico2d import *
import game_framework

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


Background_image = [Map(320,288,17,304,1360,3362,17,3058) for i in range(0,2)]
order = None

def enter():
    global Background_image,order
    Background_image[0].image = load_image('./resource/image/logo.imgae_01.png')
    Background_image[1].image = load_image('./resource/image/logo.imgae_02.png')
    order = 0
    Background_image[order].image.clip_draw(Background_image[order].nowx, Background_image[order].nowy, 320, 288, 320,288)
    update_canvas()
    pass

def handle_events():
    pass

#(Npc.pngx,Npc.pngy,Npc.weight,Npc.height,Npc.mapx - Maping[round].Nowx,Npc.mapy - - Maping[round].Nowy)
def update():
    Background_image[order].nowx += 336
    if(Background_image[order].nowx >= Background_image[order].endx):
        Background_image[order].nowx = Background_image[order].startx
    delay(0.1)
    pass

def draw():
    clear_canvas()
    Background_image[order].image.clip_draw(Background_image[order].nowx,Background_image[order].nowy,320,288,320,288)
    print(Background_image[order].nowx,Background_image[order].nowy)
    update_canvas()
    delay(0.001)
    pass
