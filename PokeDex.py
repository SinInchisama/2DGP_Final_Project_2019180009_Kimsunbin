class PokeDex:
    def __init__(self):
        self.list = [False for i in range(0,27)]
        pass

    def PokeDex_check(self,Num):
        if not(self.list[Num]):
            self.list[Num] = True
