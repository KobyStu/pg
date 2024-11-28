# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text avypise ho pozpatku
#vytvorte funkce pozpatku(), ktera jako parametr bere texts vraci ho pozpatku tzn. "ahoj" --> "joha"
#osetrete chybove stavy pomoci try - except
import sys #pro parametry z prikaz řadky

def pozpatku(text):
    text_pozpatku = ""
    for pismeno in reversed(text): 
        text_pozpatku += pismeno                            
    return text_pozpatku

if __name__ == "__main__":
    try:
        soubor = sys.argv[1]
        with open(soubor,"r") as fp:
         obsah = fp.read
         obracene = pozpatku(obsah)
         print(obracene)
    except IndexError:
        print("zadej název souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")