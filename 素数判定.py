def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_prime_list(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

limit_num = 100
result = get_prime_list(limit_num)
print(f"1から{limit_num}までの素数一覧:")
print(result)
print(f"合計: {len(result)}個")
