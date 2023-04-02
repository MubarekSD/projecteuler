def even_fibonacci_numbers(n):
    """Returns the sum of all even fibonacci numbers up to n."""
    a, b = 0, 1
    total = 0
    while a < n:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


if __name__ == "__main__":
    print(even_fibonacci_numbers(4000000))
