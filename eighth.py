def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
   # if binarni_cislo == int:
    return 0

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

    #bude třeba využít zajímavější funkce/příkazy -možná nějaká knihovna?

    #zeptat se na zadání 

    #převést bin na textový řetěžec
    #jít odzadu
    #proměná součet,hodnota nula, a postupně přičítat hodnoty dle "mocnin"(když"1", záleží na pořadí)(přeskakovat nuly),