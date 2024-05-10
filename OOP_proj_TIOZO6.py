from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
    
    abstractmethod
    def get_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=5000, szobaszam=szobaszam)
    
    def get_tipus(self):
        return "Egyágyas"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=8000, szobaszam=szobaszam)
    
    def get_tipus(self):
        return "Kétágyas"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []
    
    def add_szoba(self, szoba):
        self.szobak.append(szoba)
    
    def foglalas(self, szobaszam, datum, printmessage):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum < datetime.now():
                    if printmessage:
                        print("A foglalás csak jövőbeli dátumra lehetséges!")
                    return None
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        if printmessage:
                            print("Ez a szoba már foglalt ezen a dátumon!")
                        return None
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                if printmessage:
                    print(f"{szoba.get_tipus()} szoba lefoglalva {datum.strftime('%Y-%m-%d')} dátumra. Ár: {szoba.ar}")
                return foglalas
        if printmessage:
            print("Nincs ilyen szoba!")
        return None
    
    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("A foglalás sikeresen törölve!")
            return True
        print("Nem található ilyen foglalás!")
        return False
    
    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek foglalások.")
        else:
            print("Az összes foglalás:")
            for foglalas in self.foglalasok:
                print(f"{foglalas.szoba.get_tipus()} szoba, Szobaszám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

def init(szalloda: Szalloda):
    szalloda.add_szoba(EgyagyasSzoba(101))
    szalloda.add_szoba(EgyagyasSzoba(102))
    szalloda.add_szoba(KetagyasSzoba(201))
   
    szalloda.foglalas(101, datetime(2024, 5, 14), False)
    szalloda.foglalas(101, datetime(2024, 5, 17), False)
    szalloda.foglalas(102, datetime(2024, 5, 18), False)
    szalloda.foglalas(201, datetime(2024, 5, 23), False)
    szalloda.foglalas(201, datetime(2024, 5, 25), False)

def main():
    
    szalloda = Szalloda("Kényelem Szálloda")

    init(szalloda)

    print("Üdvözöljük a NagyHegy Szállodában!")
    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalás lista")
        print("0. Kilépés")

        valasztas = input("Választott művelet: ")

        if valasztas == "1":
            szobaszam = int(input("Adja meg a foglalni kívánt szoba számát: "))
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
            except ValueError:
                print("Hibás dátum formátum!")
                continue
            foglalas = szalloda.foglalas(szobaszam, datum, True)
            if foglalas:
                print("Sikeres foglalás!")
            else:
                print("A foglalás sikertelen!")
        
        elif valasztas == "2":
            szobaszam = int(input("Adja meg a lemondani kívánt foglalás szobaszámát: "))
            datum = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
            except ValueError:
                print("Hibás dátum formátum!")
                continue
            for foglalas in szalloda.foglalasok:
                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    szalloda.lemondas(foglalas)
                    break
            else:
                print("Nincs ilyen foglalás!")
        
        elif valasztas == "3":
            szalloda.listaz_foglalasok()

        elif valasztas == "0":
            print("Viszlát!\nKészítette: TIOZO6")
            break
        
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
