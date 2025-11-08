import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def inserisci_valori_museo(self):
        musei = self._model.get_musei()
        self._view.drop_down_museo.options.append(ft.dropdown.Option("Nessun filtro"))
        for i in musei:
            self._view.drop_down_museo.options.append(ft.dropdown.Option(i))

    def inserisci_epoca(self):
        epoca = self._model.get_epoche()
        self._view.drop_down_epoca.options.append(ft.dropdown.Option("Nessun filtro"))
        for i in epoca:
            self._view.drop_down_epoca.options.append(ft.dropdown.Option(i))

    # CALLBACKS DROPDOWN



    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self,e):
        self._view.lista_artefatti.clean()  ##elimino precedente ricerca
        lista = self._model.get_artefatti_filtrati(self._view.drop_down_museo.value,self._view.drop_down_epoca.value)
        for i in lista:
            self._view.lista_artefatti.controls.append(ft.Text(i))
        self._view.page.update()   ##aggiorno la pagina




