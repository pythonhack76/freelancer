#from py 3.10 
def http_error(status):
    match status:
        case 400:
            print("errore 400")
        case 404:
            print("errore 404")
        case 420:
            print("errore 420")

        case _:
            print("non abbiamo avuto nessuna selezione!")


http_error(400)

#before py 3.10
def zero():
    print("zero")

def uno():
    print("uno")

def due():
    print("due")

def tre():
    print("tre")

def quattro():
    print("quattro")

options = { 0 : zero,
            1 : uno,
            2 : due,
            3 : tre, 
            4 : quattro, }


options[3]()