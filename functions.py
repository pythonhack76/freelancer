# stringa = "testo della Stringa"

# stringa.capitalize() 
# print(stringa.count("testo"))
# print(stringa)


# print("{}, il sito del professionista". format("LucaRulvoni.it"))

# str = "il testo di questo codice è statro scritto da {}"

# frase = "oggi è {} e sto programmando con {} e devo fare un {}"

# print(frase.format("giovedi","python","programma"))


# string_num = '289289289'

# print(string_num.isdigit())

# result = frase.startswith('oggii', 0)
# print(result)

# word = 'pippo@gmail.com'
# print(word.rsplit('@', 1))

# print(word.rstrip('p'))


# stringa_n = """     parole delle parole      """
# print(stringa_n)
# print(stringa_n.strip('delle'))



def is_even(list1):
    even_num = []
    for n in list1: 
        if n % 2 == 0:
            even_num.append(n)
    return even_num


even_num = is_even([2, 4, 54, 34, 65, 44, 7])
print("Even numbers are: ", even_num )


def matematica(ad1, ad2):
    add = ad1 + ad2
    sub = ad1 - ad2
    multiply = ad1 * ad2
    division = ad1 / ad2

    return add, sub, multiply, division

a, b, c, d = matematica(20, 10)

print("addizione: ", a)
print("addizione: ", b)
print("addizione: ", c)
print("addizione: ", d)
