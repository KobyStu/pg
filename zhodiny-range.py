    #1
def my_range(start,stop,step=1):
    results = []
    i = start
    while i < stop:
        results.append(i)
        i += step 
    return results

if __name__ == "_main_":
    seznam = list(range(1,10))
    print(seznam)

    seznam = my_range(1,10)
    print(seznam)

    