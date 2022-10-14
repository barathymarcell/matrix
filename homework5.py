def developer():
    print("-- Developer létrehozva --")

class Team:
    def __init__(self, nev , projekt, kor):
        self._nev = nev
        self._projekt = projekt
        self._kor = kor

    def __eq__(self, masik_dolgozo):
        if self._projekt == masik_dolgozo._projekt:
            print(self._nev, "és", masik_dolgozo._nev, "dolgoznak egy projekten.")

dolgozo1 = Team("Ricsi", "SolArch", "Frontend")
dolgozo2 = Team("Angéla", "ZerTeng", "Teszteló")
dolgozo3 = Team("Peti", "KefERP", "Backend")
dolgozo4 = Team("Éva", "KefERP", "Frontend")

developer()
print(dolgozo1._nev, "a", dolgozo1._projekt, "-en dolgozik", dolgozo1._kor,"szerepkörben")
developer()
print(dolgozo2._nev, "a", dolgozo2._projekt, "-en dolgozik", dolgozo2._kor,"szerepkörben")
developer()
print(dolgozo3._nev, "a", dolgozo3._projekt, "-en dolgozik", dolgozo3._kor,"szerepkörben")
developer()
print(dolgozo4._nev, "a", dolgozo4._projekt, "-en dolgozik", dolgozo4._kor,"szerepkörben")
print()
print(dolgozo3 == dolgozo4)
