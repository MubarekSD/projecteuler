def multiples_of_3_and_5(n):
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


if __name__ == "__main__":
    print(multiples_of_3_and_5(1000))
