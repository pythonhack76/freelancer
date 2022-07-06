bits = [True, False, False, True, True, False, False, False, True]
#elenco iniziale
elenco = ['Paolo','Giorgia','Filippo','Enzo','Maria','Luca']
#creazione di un elenco di eccezioni 
eccezioni = ['Luca','Andrea']
new_bits = []

super_bits = [1 if b == True else 0 for b in bits]

#creazione nuova lista con esito confronto 
add_sig = []

for b in bits: 
    if b == True: 
        new_bits.append(1)
    else:
        new_bits.append(0)

# print(bits)
# print(new_bits)

#ciclo di partenza
for nome in elenco:
    #verifica ultimo carattere     
    if nome[-1] == 'a':
        #confronto tra lista e lista delle eccezioni 
        for j in eccezioni:
            if(nome == j):
              add_sig.append('Sig.ra')
            else:
              add_sig.append('Sig.re')

print(elenco)
print(add_sig)
print(super_bits)

