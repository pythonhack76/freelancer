from database import *

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
            persona = {
                "nome": self.nome,
                "cognome": self.cognome,
                "sesso": self.sesso,
                "anni": self.anni,
                "nascita": self.nascita,
                "indirizzo": self.indirizzo,
                "email": self.email

            }
            for key, value in persona.items():
                print(f'{key}={value}')
        except:
            print("except")
        finally: 
            print("finally")

class Lavoro:
    def __init__(self, titolo = 'null', desc = 'null', price = 0, location = 'null'):
        self.titolo = str(titolo)
        self.desc = str(desc)
        self.price = int(price)
        self.location = str(location)  

    def creaLavoro(self):
        print('test crea lavoro')



p1 = Persona('luca','rulvoni')
p1.creaPersona() 
p2 = Lavoro('developer') 
p2.creaLavoro()

c1 = Connessione()