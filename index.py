from functools import lru_cache
from mailbox import NotEmptyError


class Freelance:
    def __init__(self):
        self.nome = ''
        self.cognome = ''
        self.indirizzo = ''
        self.email = ''
        self.mobile = 000000


    def creaFreelance(self, nome, cognome, email):
        freelances = {'nome:':'', 'cognome:': '', 'email:': ''}
        max_numbers = 10
        conta_valori = len(freelances)
        print(conta_valori, '/n')
        while conta_valori <= max_numbers:
            
            nome = input('inserisci nome: ')
            cognome = input('inserisci cognome: ')
            email = input('inserisci email: ')
            d2 = {'nome:':nome,'cognome:':cognome,'email:':email}
            freelances.update(**d2)
            #print(freelances)
            for k in freelances.items():
            print(k)
        

new_freelance = Freelance() 
new_freelance.creaFreelance('','','') 
