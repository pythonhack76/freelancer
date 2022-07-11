class Libro:
    def __init__(self, titolo, autore, genere):
        self.titolo = titolo
        self.autore = autore
        self.gneere = genere

    def viewLibro(self):
        print(f'il mio autore preferito, {self.autore}, ha scritto {self.titolo}')

    
libro1 = Libro("Shining","King","Horror")
libro1.viewLibro() 

