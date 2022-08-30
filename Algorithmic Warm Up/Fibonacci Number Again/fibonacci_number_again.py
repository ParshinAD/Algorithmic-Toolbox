# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current



def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    seq = [0, 1]
    frst, scnd = 0, 1
    flg = True
    while (frst != 0 or scnd != 1) or flg:
        frst, scnd = scnd, (frst+scnd) % m
        flg = False
        seq.append(scnd)
    seq = seq[:-2]
    return seq[n % len(seq)]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
