def arithmetic_sum(a, d, n):
    s = 0
    while n > 0:
        s += a + (n - 1) * d
        n -= 1
    return s


if __name__ == "__main__":
    result = arithmetic_sum(-5, -2, 20)
    print(result)