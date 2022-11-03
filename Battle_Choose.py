import Choose_Poketmon
from pico2d import *

def enter():
    Choose_Poketmon.enter()

def handle_events():
    global CusorY, frame
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
                print(CusorY)
            elif event.key == SDLK_UP:
                if (CusorY > 0):
                    CusorY -= 1
            elif event.key == SDLK_a:
                if (CusorY != 6):
                    game_framework.push_state(Status_state)
                    # frame = 645       # 포켓몬 선택하고 무슨 행동할지 선택하는 창
                elif (CusorY == 6):
                    game_framework.pop_state()
    pass

def draw():
    Choose_Poketmon.draw()

def update():
    Choose_Poketmon.update()

def exit():
    pass

def resume():
    pass

def pause():
    pass