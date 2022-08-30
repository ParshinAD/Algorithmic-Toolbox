# python3
import random

def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    lhd = 0
    rhd = 1
    for _ in range(n):
        lhd, rhd = rhd, lhd+rhd
    return lhd


if __name__ == '__main__':
    # while True:
    #     n = random.randint(0, 10)
    #     print(n)
    #     if fibonacci_number_naive(n) == fibonacci_number(n):
    #         print('OK')
    #     else:
    #         print('Wrong answer:', fibonacci_number_naive(n), fibonacci_number(n))

    input_n = int(input())
    print(fibonacci_number(input_n))
