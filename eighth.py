def bin_to_dec(binarni_cislo):
    # Převod binárního čísla na celé desítkové číslo
    # Pokud je vstup typu int, převedeme ho na string
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)

    # Ověření, že vstup obsahuje pouze '0' a '1'
    if not all(char in '01' for char in binarni_cislo):
        raise ValueError("Input must be a binary number (string or integer).")

    decimal_value = 0  # Inicializace desítkového výsledku
    length = len(binarni_cislo)  # Délka binárního čísla

    # Procházení binárního čísla od nejvyššího bitu k nejnižšímu
    for i, digit in enumerate(binarni_cislo):
        if digit == '1':
            # Umocnění 2 na pozici (length - 1 - i) a přičtení k výsledku
            power = length - 1 - i
            value = 2 ** power
            decimal_value += value
    return decimal_value

def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157  # Test for binary 10011101
    assert bin_to_dec(10011101) == 157    # Test for integer 10011101

# Spuštění testů
test_funkce()