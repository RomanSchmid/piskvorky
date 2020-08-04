import util
from random import randrange

def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pc_tah = randrange(0, 19)
    while pole[pc_tah] != '-':
        pc_tah = randrange(0, 19)

    return util.tah(pole, pc_tah, 'o')