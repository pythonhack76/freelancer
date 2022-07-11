import numpy as np

class Item:
    def __init__(self, nome, prezzo=0, qta=0, stock=0):
        self.nome = nome
        self.prezzo = prezzo
        self.qta = qta
        self.stock = stock
       

    def singular(self, result=0):
        self.result = result
        if result (self.qta <= 1):
            print("pezzo")
        else:
            print("pezzi")


    def calculate_total_price(self):
        res = (f'il mio risultato è pari a {self.qta} {self.result}' + '\n')
        print(res)
        return self.prezzo * self.qta + self.stock
        
      
 

class Sellers:
    pass


item1 = Item("Telefono", 100, 2, 2, '') 
item1_price = 30
item1_quantity = 1

print(item1.calculate_total_price())



