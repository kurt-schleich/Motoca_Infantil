from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.cheio = None
        self.duracao = 0
        self.consumo = 0
        self.escrito = 0

    def inserir (self, grafite: Grafite):
        if grafite.getCalibre() == self.calibre:
            if not self.cheio:
                self.cheio = True
                self.duracao = grafite.getTamanho()
                self.consumo = grafite.getDureza()
                self.escrito = 0
                return True
            else:
                return False
        else:
            return False

    def remover(self):
        if self.cheio:
            self.cheio = None
            return True
        else:
            return False

    def escrever(self, folhas: int):
        if self.cheio:
            for i in range(0, folhas):
                self.duracao -= self.consumo
                self.escrito += 1
                if self.duracao <= 0:
                    break
            if self.duracao == 0:
                self.cheio = None
                if self.escrito != folhas:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False

    def getGrafite(self):
        return self.cheio

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.escrito
