import util
import ai

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

    return util.tah(pole, kam_hrat, 'x')


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    herni_pole = '-' * DELKA_POLE

    while True:
        herni_pole = tah_hrace(herni_pole)
        if vyhodnot(herni_pole) != '-':
            break
        print(herni_pole)

        herni_pole = ai.tah_pocitace(herni_pole)
        if vyhodnot(herni_pole) != '-':
            break
        print(herni_pole)
    
    print(herni_pole)
    print("Vítězem je", vyhodnot(herni_pole))