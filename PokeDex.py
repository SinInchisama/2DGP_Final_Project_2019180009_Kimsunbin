from pico2d import *

class PokeDex:
    image = None
    Scene = 0
    Catch = 0
    def __init__(self):
        self.list = [0 for i in range(0,27)]
        if PokeDex.image == None:
            PokeDex.image = load_image('./resource/image/PokeDex.png')
        pass

    def PokeDex_View_check(self,Num):
        if  (self.list[Num] == 0):
            self.list[Num] = 1
            PokeDex.Scene += 1

    def PokeDex_Catch_check(self,Num):
        if  (self.list[Num] != 2):
            self.list[Num] = 2
            if(self.list[Num] == 1):
                PokeDex.Scene -= 1
            PokeDex.Catch += 1
            PokeDex.Scene += 1
