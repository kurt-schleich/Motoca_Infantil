from enum import Enum


class Dureza(Enum):
    G_HB = 1
    G_2B = 2
    G_4B = 4
    G_6B = 6
    G_dbg = 8

    def __init__(self, Dureza):
        self.Dureza = Dureza

    def getdureza(self):
        return self.Dureza
