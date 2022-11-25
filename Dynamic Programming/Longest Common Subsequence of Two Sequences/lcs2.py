# python3
import numpy as np


def way(d, i, j):
    if i == 0 or j ==0:
        return []
    elif d[i, j] == d[i-1, j] + 1:
        result = way(d, i-1, j)
    elif d[i, j] == d[i, j-1] + 1:
        result = way(d, i, j-1)
    else:
        result = way(d, i-1, j-1)
        if d[i, j] == d[i-1, j-1]:
            result = result + [(i, j)]
    return result


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    n, m = len(first_sequence), len(second_sequence)
    d = np.zeros((n+1, m+1))
    d[:, 0] = list(range(n + 1))
    d[0, :] = list(range(m + 1))
    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = d[i, j - 1] + 1
            deletion = d[i - 1, j] + 1
            match = d[i - 1, j - 1]
            mismatch = d[i - 1, j - 1] + 2
            if first_sequence[i - 1] == second_sequence[j - 1]:
                d[i, j] = min(insertion, deletion, match)
            else:
                d[i, j] = min(insertion, deletion, mismatch)
    return len(way(d, n, m))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
