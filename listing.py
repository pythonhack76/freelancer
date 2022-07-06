
# lista_immobili = ['torino','milano1','milano2','roma-trasvere']
# lista_agenti = []
# lista_clienti = []
# immobile = 0


# def add_immobili():
#     immobile = str(input("inserisci : "))
#     lista_immobili.append(immobile)

# def view_immobili():
#     for i in range(immobile):
#         print(lista_immobili[i])


# add_immobili()
# view_immobili() 

def add_items():
    global shopList
    shopList = [] 
    maxLengthList = 6
    while len(shopList) < maxLengthList:
        item = input("Enter your Item to the List: ")
        shopList.append(item)
        print(shopList)
    print("That's your Shopping List")
    print(shopList)

def view_items():
    shopList1 = []
    for i in shopList1:
        if len(shopList1) < 0:
            print("non ci sono rticoli")
        else:
            print(i)



#add_items()
view_items() 


