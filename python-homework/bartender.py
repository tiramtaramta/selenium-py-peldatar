"""
A feladatokat külön python fileban oldd meg. Minden feladat tartalmazza az elvárt filenevet.
Ezen a néven fogadható el a megoldás.

Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik. Kétféle italt ismerünk: sör és kóla.
Ha a felhasználó kiskorú, és sört kér, akkor közöld vele, hogy sajnos nem adhatsz neki.
Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele, hogy a koffein megemelheti a vérnyomását.
Ha ismeretlen italt adott meg, akkor írd ki, hogy csak sört és kólát tudunk adni. Minden más esetben szolgáld ki.
(Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")
A megoldást egy bartender.py nevű file-ban kell beadnod.
"""

kor = int(input("Adja meg az életkorát: "))
ital = input("Mit szeretne inni? ")
s = "sör"
k = "kóla"

if ital == s or ital == k:
    if ital == k:
        if kor <= 60:
            print("Parancsoljon, itt a kólája!")
        else:
            print("A koffein megemelheti a vérnyomását.")
    if ital == s:
        if kor < 16:
            print("Sajnálom, de nem adhatok sört.")
        else:
            print("Parancsoljon, itt a söre!")
else:
    print("Csak sört, vagy kólát szolgálunk fel!")
