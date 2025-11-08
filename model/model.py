from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        lista = self._artefatto_dao.accesso_dati()  ##lista artefatti
        lista2 = self._museo_dao.accesso_dati()    ##lista musei
        lista_filtrata = []
        if museo!="Nessun filtro" and epoca != "Nessun filtro": ##faccio filtro e separo diversi casi di scelta
            valore = ""
            for i in lista2:
                if museo == i.nome:     ##vado a ricercare lid museo esatto in modo da poter attuare il confronto
                    valore = i.id     ##per fare ciò ho dovuto però modificare i dati forniti dalla tabella
                else:              ##infatti la tabella artefatto e la tabella museo avevano per i campi id_museo
                    pass         ##valori completamente diversi (non ho trovato altro modo)
            for i in lista:
                if i.id_museo == valore and i.epoca == epoca:  ##se i valori sono uguali...
                    lista_filtrata.append(i)              ##...sono in presenza di un elemento ricercato
                else:
                    pass
        elif museo == "Nessun filtro" and epoca != "Nessun filtro": ##se inserisco solo Nessun filtro per museo
            for i in lista:
                if i.epoca == epoca:
                    lista_filtrata.append(i)  ##restituisco elenco filtrato solo su epoche
                else:
                    pass
        elif museo != "Nessun filtro" and epoca == "Nessun filtro":
            valore = ""          ##lid del museo
            for i in lista2:
                if museo == i.nome:
                    valore = i.id
                else:
                    pass
            for i in lista:
                if i.id_museo == valore:
                    lista_filtrata.append(i)
                else:
                    pass
        else:
            lista_filtrata = self._artefatto_dao.accesso_dati()

        return lista_filtrata


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        lista_epoche = self._artefatto_dao.accesso_epoche()
        return lista_epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        nomi = []
        lista = self._museo_dao.accesso_dati()
        for i in lista:
            nomi.append(i.nome)     ##decido per ordine e chiarezza di inserire nella dropdown solo
        return nomi                ##il nome del museo




