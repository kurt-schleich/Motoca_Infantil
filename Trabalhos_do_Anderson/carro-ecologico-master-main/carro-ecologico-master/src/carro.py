class Carro:

    def __init__(self):
        self.passageiros = 0
        self.combustivel = 0
        self.quilometragem = 0

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros = self.passageiros + 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros = self.passageiros - 1
            return True
        else:
            return False

    def dirigir(self, percurso):
        if self.passageiros == 0 or self.combustivel == 0:
            return False

        else:
            if self.combustivel - percurso < 0:
                self.quilometragem = self.quilometragem + (self.combustivel)
                self.combustivel = 0
                return False

            else:
                self.quilometragem = self.quilometragem + percurso
                self.combustivel = self.combustivel - percurso
                return True

    def abastecer(self, quantia):
        if quantia > 0:
            self.combustivel += quantia
            if self.combustivel > 100:
                self.combustivel = 100
            return True
        else:
            return False