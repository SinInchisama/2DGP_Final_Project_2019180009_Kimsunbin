from pico2d import *
import game_framework
import play_state

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

def enter():
    pass

def handle_events():
    events = get_events()
    for event in events:
        pass

def update():
    pass

def draw():
    pass

def exit():
    pass