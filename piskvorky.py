from random import randrange

DELKA_POLE = 20

SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"

def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """

    if 'xxx' in pole:
        return "x"
    elif 'ooo' in pole:
        return "o"
    elif 'xxx' in pole and 'ooo' in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    cast1 = pole[:cislo_policka]
    cast2 = pole[cislo_policka + 1:]

    vysledne_pole = cast1 + symbol + cast2
    return vysledne_pole


def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    while True:
        kam_hrat = int(input("Kam chceš hrát? "))
        if kam_hrat <= 19 and kam_hrat >= 0:
            if pole[kam_hrat] == '-':
                break
            print("Toto pole je obsazené, zkus to znovu")
        print("Zadej číslo mezi 0 a 19")

    return tah(pole, kam_hrat, 'x')

def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pc_tah = randrange(0, 19)
    while pole[pc_tah] != '-':
        pc_tah = randrange(0, 19)

    return tah(pole, pc_tah, 'o')


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    herni_pole = '-' * DELKA_POLE

    while vyhodnot(herni_pole) == '-':
        herni_pole = tah_hrace(herni_pole)
        print(herni_pole)
        herni_pole = tah_pocitace(herni_pole)
        print(herni_pole)
        
    print("Vítězem je", vyhodnot(herni_pole))


#if __name__ == "__main__":
piskvorky1d()
