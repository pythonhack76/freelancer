#maniploazione della stringa

parola_chiave = "CosaNeSappiamoDegliAlieni"

parola_chiave = "".join( [i if i.islower() else " " + i for i in parola_chiave])[1:]
parola_lower = str.lower(parola_chiave)
print(parola_lower)