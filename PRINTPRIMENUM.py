def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_prime_numbers(n):
    primes = []
    for num in range(n + 1):
        if is_prime(num):
            primes.append(num)
    print("Prime numbers from 0 to", n, "are:", primes)

# Example usage
limit = 100
print_prime_numbers(limit)
