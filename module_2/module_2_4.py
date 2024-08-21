numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Список содержащий все простые числа:
primes = []
# Список содержащий все не простые числа:
not_primes = []

for i in numbers:
    is_prime = True
    for k in range(2, i):
        if i % k == 0:
            not_primes.append(i)
            is_prime = False
            break
    if is_prime is True and i != 1:
        primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)
