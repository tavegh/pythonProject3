# csináljunk egy rendszert, ami képalbumokat kezel.
# legyenek felhasználóink, akiknek van többek között jelszavuk és ezt lehet ellenőrizni (non-public)
# a képek legyenek albumokba rendezve. Az albumokba a képeket az album(!) tulajdonosa tudja berakni vagy kivenni
# a képeknek legyen méretük, formátumuk, nevük de ezekből a méretet és a formátumot csak a kép(!) tulajdonosa tudja
# módosítani.

class Felhasznalo:
    def __init__(self, felhasznalonev, jelszo):
        self.felhasznalonev = felhasznalonev
        self._jelszo = jelszo  # Az aláhúzás jelzi, hogy ez egy nem-publikus attribútum

    def ellenoriz_jelszo(self, beirt_jelszo):
        return self._jelszo == beirt_jelszo


class Kep:
    def __init__(self, nev, meret, formatum, tulajdonos):
        self.nev = nev
        self.meret = meret
        self.formatum = formatum
        self.tulajdonos = tulajdonos

    def modosit_meret(self, uj_meret):
        # Itt lehetne ellenőrizni különböző feltételeket (pl. érvényes méret)
        self.meret = uj_meret

    def modosit_formatum(self, uj_formatum):
        # Itt lehetne ellenőrizni különböző feltételeket (pl. érvényes formátum)
        self.formatum = uj_formatum


class KepAlbum:
    def __init__(self, tulajdonos):
        self.tulajdonos = tulajdonos
        self.kepek = []

    def kep_hozzaad(self, kep):
        # Csak az album tulajdonosa adhat hozzá képet
        if kep.tulajdonos == self.tulajdonos:
            self.kepek.append(kep)
            print(f"A(z) {kep.nev} kép hozzáadva az albumhoz.")
        else:
            print("Nincs jogosultságod képet hozzáadni az albumhoz.")

    def kep_kivesz(self, kep):
        # Csak az album tulajdonosa vehet ki képet
        if kep.tulajdonos == self.tulajdonos and kep in self.kepek:
            self.kepek.remove(kep)
            print(f"A(z) {kep.nev} kép eltávolítva az albumról.")
        else:
            print("Nincs jogosultságod képet eltávolítani az albumról.")


def fohasznalo_menu():
    print("1. Képalbum létrehozása")
    print("2. Kép hozzáadása egy albumhoz")
    print("3. Kép eltávolítása egy albumból")
    print("4. Kilépés")
    valasztas = input("Válassz egy lehetőséget: ")
    return valasztas


# Példa használatra:
felhasznalo1 = Felhasznalo("user1", "password1")

kep1 = Kep("kep1", "1 MB", "JPEG", felhasznalo1)

albumok = []

while True:
    valasztas = fohasznalo_menu()

    if valasztas == "1":
        album_nev = input("Add meg az album nevét: ")
        album = KepAlbum(felhasznalo1)
        albumok.append((album_nev, album))
        print(f"Képalbum '{album_nev}' létrehozva.")

    elif valasztas == "2":
        album_nev = input("Add meg az album nevét, ahova a képet hozzá szeretnéd adni: ")
        for nev, album in albumok:
            if nev == album_nev:
                album.kep_hozzaad(kep1)

    elif valasztas == "3":
        album_nev = input("Add meg az album nevét, ahonnan a képet eltávolítanád: ")
        for nev, album in albumok:
            if nev == album_nev:
                album.kep_kivesz(kep1)

    elif valasztas == "4":
        break

    else:
        print("Érvénytelen választás. Kérlek, válassz újra.")