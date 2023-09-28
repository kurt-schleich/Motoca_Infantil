from item import Item
from moeda import Moeda


class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volume_MAX = volumeMaximo
        self.volume_usado = 0
        self.armazenado = []
        self.val = 0
        self.inteiro = True
    def getVolume(self):
        return self.volume_usado

    def getVolumeMaximo(self):
        return self.volume_MAX

    def getVolumeRestante(self):
        return self.volume_MAX - self.volume_usado

    def add_I(self, item: Item):
        if self.inteiro:
            if self.getVolumeRestante() > item.get_volume():
                self.armazenado.append(item.get_nome())
                self.volume_usado += item.get_volume()
                return True
            else:
                return False
        else:
            return False

    def add_M(self, moeda: Moeda):
        if self.inteiro:
            if moeda == Moeda.M100:
                self.val += 1
                self.volume_usado += 4
            elif self.getVolumeRestante() > moeda.get_vol():
                self.val += moeda.get_valor()
                self.volume_usado += moeda.get_vol()
                return True
            else:
                return False
        else:
            return False

    def obterItens(self):
        if not self.inteiro:
            itens = []
            for i in self.armazenado:
                if isinstance(i, str):
                    itens.append(i)
            if itens != []:
                b = ''
                for i in range(len(itens)-1):
                    b = b + itens[i] + ', '
                b += itens[-1]
                return b
            else:
                return 'vazio'
        else:
            return None

    def obterMoedas(self):
        if not self.inteiro:
            val = self.val
            self.val = 0
            return val
        else:
            return -1

    def taInteiro(self):
        return self.inteiro

    def quebrar(self):
        if self.inteiro:
            self.inteiro = False
            return True
        else:
            return False
