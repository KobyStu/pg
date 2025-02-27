def obvod_ctverce(delka_strany):
# funkce vypocita obvod ctverce z delky jeho strany
    vysledek = None
    vysledek = 4*delka_strany
    return vysledek


def obsah_ctverce(delka_strany):
# funkce vypocita obsah ctverce z delky jeho strany
    vysledek = None
    vysledek = delka_strany**2
    return vysledek


def pocet_pismen(text, pismeno):
    # funkce vrati pocet vyskytu pismene v textu
    return text.count(pismeno) #v1
   #pocet = 0
   #for p in text:
   #   if p == pismeno:
   #       pocet += 1
   #return pocet                #v2

def index_pismene(text, pismeno):
    # funkce vrati indexy daneho pismene v textu, tzn. pro text="ahoj, honzo" a pismeno="h" vrati [1, 6]
    vyskyt = []
    for index, znak in enumerate(text):
        if znak == pismeno:
            vyskyt.append(index)
    return vyskyt

def fibonachi(maximum):
    result = [1,1]
    soucet = result[-2] + result[-1]
    while soucet <= maximum:
        result.append(soucet)
        soucet = result[-2] + result[-1]
    return result

if __name__ == "__main__":
    index_pismene("ahoj, honzo", "h")