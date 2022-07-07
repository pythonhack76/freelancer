import sqlite3
import os


class Connessione:
    def __init__(self):
        try:
            #connessione 
            connessione = sqlite3.connect("database.db")
            cursor = connessione.cursor() 
            print('inizializzato...')            
            #chiusura database
            cursor.close()
        except sqlite3.Error as error:
            print("Errore" , error)
        finally:
            if connessione:
                connessione.close()
                print("la connessione al db è terminata!")

    #creo tabella utenti
    def crea_tabella_persone(self):
        try:
            pass
        except:
            pass
        finally:
            pass
    #funzione per aggiungere nuovo utente
    def addUtente(self):
        try:
            pass
        
        except sqlite3.Error as error:
            print("Errore" , error)
        finally:
            pass

    def modUtente(self):
        try:
            pass
        except sqlite3.Error as error:
            print("Errore" , error)
        finally:
            pass
    
    def delUtente(self):
        try:
            pass
        except sqlite3.Error as error:
            print("Errore" , error)
        finally:
            pass