def je_prvocislo(n):
    if n <= 1:
        return False  # 1 and níže nejsou prvočísla
    for i in range(2, int(n**0.5) + 1):   # Zkontrolujte, zda se vyskytují činitelé až do druhé odmocniny z n -> potenciální dělitelé (a*a)
        if n % i == 0:
            return False  # n je dělitelné i, tudíž není prvočíslo
    return True  # n is prime

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    prvocisla = []
    for num in range(1, maximum + 1):
        if je_prvocislo(num):
            prvocisla.append(num)  # Přidá prvočíslo do seznamu
    return prvocisla

# Example usage:
if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)


