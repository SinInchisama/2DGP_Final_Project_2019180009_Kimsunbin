from pico2d import *
import play_state
from Map import Maping
import game_framework
import Font
import Poketmon


CursorY = None
Prange = None
frame,exiting,Minus = None,None,None

def enter():
    global CursorY,Prange,frame,exiting,Minus
    exiting = False
    CursorY,frame = 0,0
    Prange = 0
    Minus = 486 / 26
    pass
def exit():
    pass

def draw():
    clear_canvas()

    if(frame<10):
        Maping[18].map.clip_draw(0,0,640,576,320,288)
    else:
        play_state.Pokedex.image.clip_draw(176,1759,160,144,320,288,640,576)
        play_state.Pokedex.image.clip_draw(344,1881,89,22,430,500 - 80 * (CursorY),356,80)       # Cursor
        play_state.Pokedex.image.clip_draw(371, 1834, 5, 5, 626, 550 - (Minus * (Prange + CursorY)), 20, 20)  # Cursor
        for i in range(0 + Prange,6+ Prange):
            if(play_state.Pokedex.list[i] == 0):
                Font.Draw_question(8,285,500 - 80 *(i-Prange),32,32)
            else:
                Font.Draw_Al(Poketmon.Poket_Data[i].name,285,500-80*(i-Prange),32,32)
                if (play_state.Pokedex.list[i] == 2):
                    play_state.Pokedex.image.clip_draw(345,1818,5,6,260,500-80*(i-Prange),10,12)

        if(play_state.Pokedex.list[CursorY + Prange] != 0):
            Poketmon.Data.image.clip_draw(Poketmon.Poket_Data[CursorY + Prange].Pngx, Poketmon.Poket_Data[CursorY + Prange].Pngy, 56, 56, 125, 432, 224,224)
        Font.Draw_Num(play_state.Pokedex.Scene,215,160,32,32)
        Font.Draw_Num(play_state.Pokedex.Catch, 215, 75, 32, 32)
    delay(0.03)
    update_canvas()
    pass
def resume():
    pass
def pause():
    pass
def handle_events():
    global CursorY,frame,exiting,Prange
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                frame = 0
                exiting = True
            elif event.key == SDLK_DOWN:
                if(CursorY != 5):
                    CursorY += 1
                elif(Prange<21):
                    Prange += 1
            elif event.key == SDLK_UP:
                if (CursorY != 0):
                    CursorY -= 1
                elif(Prange>0):
                    Prange -= 1
    pass
def update():
    global frame
    frame += 1
    if(exiting == True and frame >10):
        game_framework.pop_state()
    pass