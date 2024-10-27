def is_prime(funk):
    def wrapper(*args, **kwargs):
        res = funk(*args, **kwargs)
        if res < 2:
            print('Не простое, не составное')
            return res
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                print('Составное')
                return res
        print('Простое')
        return res
    return wrapper


@ is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
