import game_framework
from pico2d import *
import play_state
import Font
from Map import Maping
import Poketmon

Cursor_image = None
Cursory = None

def enter():
    global Cursor_image,Cursory
    Cursor_image = load_image('./resource/image/Cursor.png')
    Cursory = 0
    pass

def handle_events():
    global Cursory

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_UP:
                if(Cursory != 0):
                    Cursory -= 1
            elif event.key == SDLK_DOWN:
                if(Cursory != 2):
                    Cursory += 1
            elif event.key == SDLK_a:
                play_state.hero.Pcount = 1
                play_state.hero.pList = [Poketmon.Tr_Poketmon(Cursory * 3,5,30,0)]
                play_state.hero.pList[0].ailment = ''
                play_state.hero.pList[0].Set_ability()
                play_state.hero.pList[0].Skill_List = [32,34,36]
                play_state.hero.pList[0].PP_list = [25,35]
                play_state.hero.pList[0].Hp = play_state.hero.pList[0].MaxHp
                Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Met = True
                play_state.Pokedex.PokeDex_Catch_check(Cursory * 3)
                game_framework.pop_state()



def draw():
    clear_canvas()

    play_state.draw_world()
    play_state.Board.clip_draw(0, 1, 83, 76, 320, 75, 644, 140)
    Maping[play_state.round].Npc[play_state.hero.Meet_Npc].Draw()

    play_state.Board.clip_draw(0, 1, 83, 76, 480, 210, 320, 140)
    Font.Draw_Al('Chikorita',380,250,16,16)
    Font.Draw_Al('Cyndaquil', 380, 210, 16, 16)
    Font.Draw_Al('Totodile', 380, 170, 16, 16)

    Cursor_image.clip_draw(0, 0, 32, 32, 360, 250 - (Cursory * 40), 16, 16)
    update_canvas()
    pass

def update():
    pass

def exit():
    pass