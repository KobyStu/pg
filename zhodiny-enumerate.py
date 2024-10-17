def my_enumerate(iterable,start=0):
    results = []
    index = start
    for value in iterable:
        results.append( (index, value))
        index += 1
    return results

def my_enumerate(iterable,start=0):
    results = []
    i = 0
    while i <len(iterable):
        results.append((i,iterable[i]))
        i += 1
    return results

if __name__ == "_main_":
    seznam = list(enumerate(["ahoj","cau","jak","se","mas"]))
    print(seznam)
    seznam = my_enumerate(["ahoj","cau","jak","se","mas"],start=2)
    print(seznam)