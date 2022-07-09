class Item:
    def __init__(self, nome, prezzo=0, qta=0, stock=0):
        self.nome = nome
        self.prezzo = prezzo
        self.qta = qta
        self.stock = stock

    def calculate_total_price(self):
        return self.prezzo * self.qta + self.stock


class Sellers:
    pass


item1 = Item("Telefono", 100, 3, 2) 
item1_price = 30
item1_quantity = 10

print(item1.calculate_total_price())


