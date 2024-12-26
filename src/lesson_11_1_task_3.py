
def primes():
    """Генератор, который генерирует последовательность простых чисел."""

    n = 2
    primes_list = []
    while True:
        if all(n % p != 0 for p in primes_list):
            yield n
            primes_list.append(n)
        n += 1


p = primes()
for i in range(10):
    print(next(p))
