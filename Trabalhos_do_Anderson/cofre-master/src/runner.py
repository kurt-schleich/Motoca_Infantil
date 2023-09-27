from src.cofre import Cofre
from src.item import Item
from src.moeda import Moeda

if __name__ == '__main__':
    '''cofre = Cofre(20)
    print(cofre)
    cofre.add_M(Moeda.M10)
    print(cofre.getVolumeRestante())
    cofre.add_M(Moeda.M50)
    print(cofre.getVolumeRestante())
    print(cofre)

    cofre.add_I(Item("ouro", 3))
    print(cofre.getVolumeRestante())
    print(cofre)

    cofre.add_I(Item("passaporte", 2)
    print(cofre.getVolumeRestante())
    print(cofre)'''
    cofre = Cofre(4)
    print(cofre.getVolumeRestante())
    cofre.add_M(Moeda.M100)
    print(Moeda.M100.get_vol())
    print(cofre.getVolumeRestante())
    passporte = Item("Passaporte", 5)
    print(cofre.getVolumeRestante())
    cofre.add_M(Moeda.M10)
    print(cofre.getVolumeRestante())

    '''if not cofre.obterItens():
        print("Voce deve quebrar o cofre primeiro")

    if cofre.obterMoedas() == -1:
        print("Voce deve quebrar o cofre primeiro")

    print(cofre)

    cofre.quebrar()
    cofre.quebrar()

    print(cofre.obterItens())
    print(cofre.obterMoedas())
    print(cofre)'''