class Persona:
    def __init__(self, nome = 'null', cognome = 'null', sesso = 'null', anni = 'null', nascita = 'null', indirizzo = 'null', email = 'null'):
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.anni = anni
        self.nascita = nascita
        self.indirizzo = indirizzo
        self.email = email 
    
    def creaPersona(self):
        try:
            print("try")
        except:
            print("except")
        finally: 
            print("finally")


p1 = Persona()
p1.creaPersona() 