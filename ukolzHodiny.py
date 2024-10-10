# funkce vrati treti prvek ze seznamu, pokud ma mene nez 3 prvky, vrati None
def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    else:
        return seznam[2]


# funkce spocita prumer z hodnot v seznamu, pouzijte sum(), len()
def udelej_prumer(seznam):
    return sum(seznam)/len(seznam)


# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
#není kompletní
    jmeno = student["jmeno"]
    prijmeni = student["prijmeni"]
    #atd.

if __name__ == "__main__":
    seznam = [9,8,5,7]
    vysledek = vrat_treti(seznam)
    #print(vysledek)

    obalka = [9,8,7,10]
    vysledek = udelej_prumer(obalka)
    #print(vysledek)

#na treti ulohu
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }

    vysledek = naformatuj_text(slovnik)
    print(vysledek)

    student["vek"] # -> 21
    student["znamky"] # -> [1, 2, 1, 1, 3, 2]
    student["znamky"][2] # -> 1

    a = 1
    f"Naformatovany retezes s hodnotou {a}" # ""Naformatovany retezes s hodnotou 1"