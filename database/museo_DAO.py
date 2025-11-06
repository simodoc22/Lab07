from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def accesso_dati(self):
        lista = []
        cnx = ConnessioneDB.get_connection()
        cursore = cnx.cursor(dictionary=True)
        query = "SELECT * FROM museo"
        cursore.execute(query)
        for museo in cursore:
            id= museo['id']
            nome= museo['nome']
            tipologia= museo['tipologia']
            oggetto = Museo(id, nome, tipologia)
            lista.append(oggetto)
        return lista
