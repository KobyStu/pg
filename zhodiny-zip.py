def my_zip(*iterables):
    results = []
    length = len(iterable[0]) #5
    i = 0
    while i < length:
        subresult = []   #Jde po sloupcích ve třech polích a dvá dohromady, "i" se stupňuje a "posouvá"
        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult))
        i += 1
    return results

if __name__ == "_main_":
    jmena = ["Alice", "Bob", "Karel", "Eva","Martin"] # ->len() -> 5
    vek   = [     30,   20,     24,     18,     27  ]
    vaha  = [     50,   80,     90,     55,     67  ]

    vysledek = list( zip(jmena, vek, vaha) )

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)

