from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass
    def accesso_dati(self):
        lista = []
        cnx = ConnessioneDB.get_connection()
        cursore = cnx.cursor(dictionary=True) ##creo un cursore di tipo dizionario
        query = "SELECT * FROM artefatto"
        cursore.execute(query)
        for artefatto in cursore:
            id= artefatto['id']
            nome= artefatto['nome']
            tipologia= artefatto['tipologia']
            epoca= artefatto['epoca']
            id_museo= artefatto['id_museo']
            oggetto = Artefatto(id, nome, tipologia, epoca, id_museo) ##creo oggetto Artefatto
            lista.append(oggetto)
        return lista

    def accesso_epoche(self):
        lista = []
        cnx = ConnessioneDB.get_connection()
        cursore = cnx.cursor(dictionary=True)
        query = "SELECT epoca FROM artefatto"
        cursore.execute(query)
        for epoca in cursore:               ##in modo tale da evitare ripetizioni di epoche nella
            if epoca["epoca"] not in lista:  ##dropdown eliminimo i duplicati
                lista.append(epoca["epoca"])
            else:
                pass
        return lista



