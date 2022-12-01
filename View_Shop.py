import play_state
import game_framework
from pico2d import *
import Font

Cursor_image = None
CusorY = None
Sell = None
Sell_Count,Max_count = None,None
def enter():
    global Cursor_image, CusorY,Sell
    Cursor_image = load_image('./resource/image/Cursor.png')
    CusorY = 0
    Sell = False
    pass

def handle_events():
    global CusorY, Sell,Sell_Count,Max_count

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if(not(Sell)):
                if event.key == SDLK_DOWN:
                    CusorY = (CusorY + 1) % 8
                elif event.key == SDLK_UP:
                    CusorY -= 1
                    if(CusorY == -1):
                        CusorY = 7
                elif event.key == SDLK_a:
                    if (CusorY < 4 and play_state.hero.Gold >= play_state.hero.inventory.Ball[CusorY][0].Sell):
                        Sell = True
                        Sell_Count = 1
                        Max_count = play_state.hero.Gold // play_state.hero.inventory.Ball[CusorY][0].Sell
                    elif (CusorY >= 4 and play_state.hero.Gold >= play_state.hero.inventory.Heal[CusorY - 4][0].Sell):
                        Sell = True
                        Sell_Count = 1
                        Max_count = play_state.hero.Gold // play_state.hero.inventory.Heal[CusorY - 4][0].Sell

                elif event.key == SDLK_ESCAPE:
                    game_framework.pop_state()

            else:
                if event.key == SDLK_LEFT:
                    Sell_Count -= 1
                    if(Sell_Count == 0):
                        Sell_Count = Max_count

                elif event.key == SDLK_RIGHT:
                    Sell_Count = Sell_Count % Max_count + 1

                elif event.key == SDLK_a:
                    if (CusorY < 4):
                        play_state.hero.inventory.Ball[CusorY][1] += Sell_Count
                        play_state.hero.Gold -= (Sell_Count*play_state.hero.inventory.Ball[CusorY][0].Sell)
                        Sell = False
                    else:
                        play_state.hero.inventory.Heal[CusorY - 4][1] += Sell_Count
                        play_state.hero.Gold -= (Sell_Count * play_state.hero.inventory.Heal[CusorY - 4][0].Sell)
                        Sell = False
                elif event.key == SDLK_ESCAPE:
                    Sell = False






    pass

def update():
    pass


def draw():
    clear_canvas()


    play_state.draw_world()
    play_state.Board.clip_draw(0, 1, 83, 76, 290, 538, 166, 76)
    Font.Draw_Num(play_state.hero.Gold, 350, 538, 16, 16)
    play_state.Board.clip_draw(0, 1, 83, 76, 500, 348, 249, 456)

    a = 0
    for i in play_state.hero.inventory.Ball:
        Font.Draw_Al(i[0].name,420,530 - 50 * a,16,16)
        Font.Draw_Num(i[0].Sell, 600, 510 - 50 * a, 16, 16)
        a+=1
    a = 0
    for i in play_state.hero.inventory.Heal:
        Font.Draw_Al(i[0].name, 420, 330 - 50 * a, 16, 16)
        Font.Draw_Num(i[0].Sell, 600, 310 - 50 * a, 16, 16)
        a += 1

    Cursor_image.clip_draw(0, 0, 32, 32, 400, 530 - (50 * CusorY),16,16)

    if(Sell):
        play_state.Board.clip_draw(0, 1, 83, 76, 540, 138, 166, 76)
        Font.Draw_Num(Sell_Count, 600, 138, 16, 16)
        Font.Draw_Al('X', 480, 138, 24, 24)
    delay(0.03)
    update_canvas()
    pass

def resume():
    pass

def pause():
    pass

def exit():
    pass