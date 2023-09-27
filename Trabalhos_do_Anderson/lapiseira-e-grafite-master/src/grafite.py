from src.dureza import Dureza


class Grafite:

    def __init__(self, calibre: float, dureza: Dureza, tamanho: int):
        self.calibre = calibre
        self.Dureza = dureza.getdureza()
        self.tamanho = tamanho

    def desgastePorFolha(self):
        return self.getDureza()

    def getDureza(self):
        return self.Dureza

    def getCalibre(self):
        return self.calibre

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho:int):
        pass