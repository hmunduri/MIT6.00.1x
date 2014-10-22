def genPrimes():
    generatedPrimes = []
    if len(generatedPrimes) == 0:
        yield 2
        generatedPrimes.append(2)
    x = 2
    while True:
        for p in generatedPrimes:
            if (x % p) != 0:
                yield x
        x += 1
