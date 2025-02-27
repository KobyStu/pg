   # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

#řešení 1: Brute-force metoda -určitě jednodušší, paměť to určitě zvládne
#slovnik = {0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět", 10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct", 20: "dvacet", 21: "dvacet jedna", 22: "dvacet dva", 23: "dvacet tři", 24: "dvacet čtyři", 25: "dvacet pět", 26: "dvacet šest", 27: "dvacet sedm", 28: "dvacet osm", 29: "dvacet devět", 30: "třicet", 31: "třicet jedna", 32: "třicet dva", 33: "třicet tři", 34: "třicet čtyři", 35: "třicet pět", 36: "třicet šest", 37: "třicet sedm", 38: "třicet osm", 39: "třicet devět", 40: "čtyřicet", 41: "čtyřicet jedna", 42: "čtyřicet dva", 43: "čtyřicet tři", 44: "čtyřicet čtyři", 45: "čtyřicet pět", 46: "čtyřicet šest", 47: "čtyřicet sedm", 48: "čtyřicet osm", 49: "čtyřicet devět", 50: "padesát", 51: "padesát jedna", 52: "padesát dva", 53: "padesát tři", 54: "padesát čtyři", 55: "padesát pět", 56: "padesát šest", 57: "padesát sedm", 58: "padesát osm", 59: "padesát devět", 60: "šedesát", 61: "šedesát jedna", 62: "šedesát dva", 63: "šedesát tři", 64: "šedesát čtyři", 65: "šedesát pět", 66: "šedesát šest", 67: "šedesát sedm", 68: "šedesát osm", 69: "šedesát devět", 70: "sedmdesát", 71: "sedmdesát jedna", 72: "sedmdesát dva", 73: "sedmdesát tři", 74: "sedmdesát čtyři", 75: "sedmdesát pět", 76: "sedmdesát šest", 77: "sedmdesát sedm", 78: "sedmdesát osm", 79: "sedmdesát devět", 80: "osmdesát", 81: "osmdesát jedna", 82: "osmdesát dva", 83: "osmdesát tři", 84: "osmdesát čtyři", 85: "osmdesát pět", 86: "osmdesát šest", 87: "osmdesát sedm", 88: "osmdesát osm", 89: "osmdesát devět", 90: "devadesát", 91: "devadesát jedna", 92: "devadesát dva", 93: "devadesát tři", 94: "devadesát čtyři", 95: "devadesát pět", 96: "devadesát šest", 97: "devadesát sedm", 98: "devadesát osm", 99: "devadesát devět", 100: "sto"}

#def cislo_text(cislo):
#    x = int(cislo)
#    if x >= 0 and x <=100:
#      return slovnik[x] 
#    else:
#      return "Neplatný typ vstupu, zadejte číslo mezi 0 a 100"
        

#řešení 2: Skládací metoda -asi se na něco tímhle způsobem hodí, ale jinak moc zbytečně složitá :D
#slovniky pro pokud je číslo dvouciferné
jednotky = {0: "nula",1: "jedna", 2: "dva",3: "tři",4: "čtyři", 5: "pět",6: "šest",7: "sedm",8:  "osm",9: "devět"}
desitky = {2: "dvacet",3:  "třicet",4: "čtyřicet",5: "padesát",6: "šedesát",7: "sedmdesát",8: "osmdesát",9: "devadesát"}
vyjimky = {0: "deset",1: "jedenáct",2: "dvanáct",3: "třináct",4: "čtrnáct",5: "patnáct",6: "šestnáct",7: "sedmnáct",8: "osmnáct",9: "devatenáct"}

def cislo_text(cislo):
    cislo_int = int(cislo)
    des = cislo_int//10 #dostaneme desítky
    jed = cislo_int%10 #zbytek po čel. dělení

    if cislo_int == 100:
        return "sto"
    elif cislo_int < 10: #Pokud je číslo jednociferné
        return jednotky[cislo_int]  
    elif cislo_int >= 10 and cislo_int < 20: 
        #druhy_znak = int(cislo[1])  # druhá číslice (jednotky) > třeba mít ve formátu string ze kterého se následně určí pozice a vypíše hodnotu charakteru na této pozici  (1 = druhá)
        return vyjimky[jed]
    else:
        #prvni_znak = int(cislo[0])  # první číslice (desítky)  
        #druhy_znak = int(cislo[1])  # druhá číslice (jednotky)
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jed]

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)


#vydělit 