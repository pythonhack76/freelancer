def moltiplica(*numeri):
    risultato = 1
    for numero in numeri:
        risultato *= numero
    return risultato 


def info_pizza(nome, prezzo, ingredienti):
    print("Nome = {0}".format(nome))
    print("Prezzo = {0}".format(prezzo))
    print("Ingredienti = {0}".format(ingredienti))

ingredienti = ['pomodoro','mozzarella','patatine','acciughe']
info = {"nome": "margherita", "prezzo": 5, "ingredienti": ingredienti}

info_pizza(**info)
#print(moltiplica(3, 4, 5, 6, 21))