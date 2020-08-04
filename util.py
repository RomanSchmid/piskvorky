def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    cast1 = pole[:cislo_policka]
    cast2 = pole[cislo_policka + 1:]

    vysledne_pole = cast1 + symbol + cast2
    return vysledne_pole