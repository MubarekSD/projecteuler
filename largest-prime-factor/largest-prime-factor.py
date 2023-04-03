def largest_prime_factor(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    return n


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
