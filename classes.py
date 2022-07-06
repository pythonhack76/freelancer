class Strumento:
    def __init__(self):
        self.n_corde = 5
        self.play()

    def play(self):
        if self.n_corde <= 6:
            print("play play play") 
        else:
            print("il tuo strumento non può suonare!")

class StrumentoElettrico(Strumento):
    def __init__(self):
        super().__init__()
        self.n_corde = 8
        self.colour = ("#00000","#FFFF")
        self.__cost = 50 
        
    def playAlto(self):
        print("paly play".upper())

    
    def __secret(self):
        print("questo strumento costa €", self._Strumento__cost, "solo!")
    


new_strumento = StrumentoElettrico()
new_strumento._StrumentoElettrico__secret() 


