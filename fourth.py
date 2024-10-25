def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ_figurky = figurka["typ"]
    aktualni_pozice = figurka["pozice"]

    # Získání řádku a sloupce z pozic
    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice

    # Kontrola, zda je cílová pozice obsazena
    if cilova_pozice in obsazene_pozice:
        return False
    
#vysvětlení figurek na https://www.blackbox.ai/chat/marl7Cd #třeba vyhledat pomocí ctrl-f (hodně textu)

    if typ_figurky == "pěšec":
        # Pěšec může jít o jedno pole dopředu
        if cilovy_radek == aktualni_radek + 1 and cilovy_sloupec == aktualni_sloupec: 
            # Tento řádek kontroluje, zda se pěšec pokouší přesunout o jedno pole dopředu. 
            # To se děje, když je cílový řádek (cilovy_radek) o 1 větší než aktuální řádek (aktualni_radek) a sloupec zůstává stejný (cilovy_sloupec == aktualni_sloupec). 
            # Pokud je tato podmínka splněna, funkce vrátí True, což znamená, že tah je možný.
            return True
        # Pěšec může jít o dvě pole dopředu z výchozí pozice (řádek 2)
        if aktualni_radek == 2 and cilovy_radek == 4 and cilovy_sloupec == aktualni_sloupec: 
            #Tento řádek kontroluje, zda se pěšec pokouší přesunout o dvě pole dopředu z jeho výchozí pozice (řádek 2). 
            # Pokud je aktuální řádek 2 a cílový řádek 4, a sloupec zůstává stejný, pak je tah také povolen a funkce vrátí True.
            return True
        
    elif typ_figurky == "jezdec":
        # Jezdec se pohybuje ve tvaru "L"
        if (abs(cilovy_radek - aktualni_radek) == 2 and abs(cilovy_sloupec - aktualni_sloupec) == 1) or \
           (abs(cilovy_radek - aktualni_radek) == 1 and abs(cilovy_sloupec - aktualni_sloupec) == 2):
            #Tato podmínka kontroluje, zda se jezdec pokouší pohybovat podle pravidel šachu, která říkají, že jezdec se pohybuje ve tvaru "L". 
            # To znamená, že jezdec může skočit:
            # O dvě políčka v jednom směru (buď vertikálně nebo horizontálně) a o jedno políčko v druhém směru.
            #Nebo o jedno políčko v jednom směru a o dvě políčka v druhém směru.
                #abs() funkce se používá k určení absolutní hodnoty rozdílu mezi cílovou a aktuální pozicí, což znamená, že nezáleží na tom, zda se pohybujeme nahoru nebo dolů na šachovnici.
            return True

    elif typ_figurky == "věž":
        # Věž se pohybuje vertikálně nebo horizontálně
        if cilovy_radek == aktualni_radek:  # Horizontální pohyb
            #Tento řádek kontroluje, zda se věž pohybuje horizontálně (tj. na stejném řádku). Pokud je cílový řádek (cilovy_radek) stejný jako aktuální řádek (aktualni_radek), provede se následující kód.
            # Zkontrolujeme, zda není v cestě jiná figura
            for sloupec in range(min(aktualni_sloupec, cilovy_sloupec) + 1, max(aktualni_sloupec, cilovy_sloupec)): 
                #Tento cyklus prochází všechny sloupce mezi aktuálním sloupcem a cílovým sloupcem (vyjma těchto dvou). 
                # Používá se min a max k určení rozsahu sloupců, ve kterých se věž pohybuje
                if (aktualni_radek, sloupec) in obsazene_pozice: 
                    #Tento řádek kontroluje, zda je v cestě věže nějaká jiná figura (tj. zda je daná pozice obsazena).
                    #Pokud ano, funkce vrátí False, což znamená, že tah není možný.
                    return False
            return True
        elif cilovy_sloupec == aktualni_sloupec:  # Vertikální pohyb
            #Tento řádek kontroluje, zda se věž pohybuje vertikálně (tj. na stejném sloupci). 
            # Pokud je cílový sloupec (cilovy_sloupec) stejný jako aktuální sloupec (aktualni_sloupec), provede se následující kód.
            # Zkontrolujeme, zda není v cestě jiná figura
            for radek in range(min(aktualni_radek, cilovy_radek) + 1, max(aktualni_radek, cilovy_radek)):
                #Tento cyklus prochází všechny řádky mezi aktuálním řádkem a cílovým řádkem (vyjma těchto dvou).
                if (radek, aktualni_sloupec) in obsazene_pozice: 
                    #Tento řádek kontroluje, zda je v cestě věže nějaká jiná figura. 
                    # Pokud ano, funkce vrátí False, což znamená, že tah není možný.
                    return False
            return True

    elif typ_figurky == "střelec":
        # Střelec se pohybuje diagonálně
        if abs(cilovy_radek - aktualni_radek) == abs(cilovy_sloupec - aktualni_sloupec):  # Diagonální pohyb
            #Tento řádek kontroluje, zda se střelec pokouší pohybovat diagonálně. 
            # Diagonální pohyb znamená, že rozdíl mezi cílovým a aktuálním řádkem je stejný jako rozdíl mezi cílovým a aktuálním sloupcem. 
            # Pokud je tato podmínka splněna, provede se následující kód.
            # Zkontrolujeme, zda není v cestě jiná figura
            radek_step = 1 if cilovy_radek > aktualni_radek else -1
            sloupec_step = 1 if cilovy_sloupec > aktualni_sloupec else -1
            #Tyto řádky určují, zda se pohybujeme směrem nahoru nebo dolů (pro řádky) a směrem doprava nebo doleva (pro sloupce). radek_step a sloupec_step --
            # -- budou 1 nebo -1 v závislosti na tom, zda se cílová pozice nachází nad nebo pod aktuální pozicí, resp. vpravo nebo vlevo. 
            radek = aktualni_radek + radek_step
            sloupec = aktualni_sloupec + sloupec_step
            #Tyto řádky nastavují počáteční hodnoty pro iteraci, tedy první pozici,kterou střelec zkontroluje na své cestě k cílové pozici.
            while (radek != cilovy_radek and sloupec != cilovy_sloupec):
                #Tento cyklus pokračuje, dokud nedosáhneme cílové pozice. Kontroluje každou pozici na cestě střelce.
                if (radek, sloupec) in obsazene_pozice:
                    #Tento řádek kontroluje, zda je na aktuální pozici na cestě obsazena jinou figurou. 
                    #Pokud ano, funkce vrátí False, což znamená, že tah není možný.
                    return False
                radek += radek_step
                sloupec += sloupec_step
                #Tyto řádky posunou pozici o jeden krok dál v diagonálním směru
            return True
            #Pokud cyklus skončí a nenajde žádnou obsazenou pozici, funkce vrátí True
            
    elif typ_figurky == "dáma":

        # !!!! Dáma kombinuje pohyb věže a střelce - tedyi popisky by byly stejné viz. výše !!!!!

        if cilovy_radek == aktualni_radek or cilovy_sloupec == aktualni_sloupec:  # Horizontální nebo vertikální pohyb
            if cilovy_radek == aktualni_radek:  # Horizontální pohyb
                for sloupec in range(min(aktualni_sloupec, cilovy_sloupec) + 1, max(aktualni_sloupec, cilovy_sloupec)):
                    if (aktualni_radek, sloupec) in obsazene_pozice:
                        return False
                return True
            elif cilovy_sloupec == aktualni_sloupec:  # Vertikální pohyb
                for radek in range(min(aktualni_radek, cilovy_radek) + 1, max(aktualni_radek, cilovy_radek)):
                    if (radek, aktualni_sloupec) in obsazene_pozice:
                        return False
                return True
        elif abs(cilovy_radek - aktualni_radek) == abs(cilovy_sloupec - aktualni_sloupec):  # Diagonální pohyb
            radek_step = 1 if cilovy_radek > aktualni_radek else -1
            sloupec_step = 1 if cilovy_sloupec > aktualni_sloupec else -1
            radek = aktualni_radek + radek_step
            sloupec = aktualni_sloupec + sloupec_step
            while (radek != cilovy_radek and sloupec != cilovy_sloupec):
                if (radek, sloupec) in obsazene_pozice:
                    return False
                radek += radek_step
                sloupec += sloupec_step
            return True
        
    elif typ_figurky == "král":
        # Král se může pohybovat o jedno pole ve všech směrech
        if abs(cilovy_radek - aktualni_radek) <= 1 and abs(cilovy_sloupec - aktualni_sloupec) <= 1:
            #Tato podmínka kontroluje, zda je cílová pozice (definována jako cilovy_radek a cilovy_sloupec) maximálně jedno políčko vzdálená od aktuální pozice
            # (definované jako aktualni_radek a aktualni_sloupec). 
            # Použití funkce abs() zajistí, že nezáleží na tom, zda se pohybujeme nahoru nebo dolů, nebo vlevo či vpravo. 
            # Pokud je splněna tato podmínka, znamená to, že král může legálně provést tento tah.
            return True
    return False  # Pokud žádné pravidlo neprošlo, tah není možný

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed 
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True