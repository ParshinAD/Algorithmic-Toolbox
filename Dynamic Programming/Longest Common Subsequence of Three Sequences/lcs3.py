# python3
import numpy as np


def way(d, i, j, z):
    if i == 0 or j ==0 or z == 0:
        return []
    elif d[i, j, z] == d[i-1, j, z] + 1:
        result = way(d, i-1, j, z)
    elif d[i, j, z] == d[i, j-1, z] + 1:
        result = way(d, i, j-1, z)
    elif d[i, j, z] == d[i, j, z-1] + 1:
        result = way(d, i, j, z-1)
    else:
        result = way(d, i-1, j-1, z-1)
        if d[i, j, z] == d[i-1, j-1, z-1]:
            result = result + [(i, j, z)]
    return result


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    n, m, s = len(first_sequence), len(second_sequence), len(third_sequence)
    d = np.zeros((n+1, m+1, s+1))
    d[:, :, 0] = np.array([list(range(i, i + m + 1)) for i in range(n + 1)])
    d[0, :, :] = np.array([list(range(i, i + s + 1)) for i in range(m + 1)])
    d[:, 0, :] = np.array([list(range(i, i + s + 1)) for i in range(n + 1)])
    for i in range(1, n+1):
        for j in range(1, m+1):
            for z in range(1, s+1):
                insertion = d[i, j - 1, z] + 1
                deletion = d[i - 1, j, z] + 1
                deletion2 = d[i, j, z-1] + 1
                match = d[i - 1, j - 1, z - 1]
                if first_sequence[i - 1] == second_sequence[j - 1] \
                        and first_sequence[i-1] == third_sequence[z-1]:
                    d[i, j, z] = min(insertion, deletion, deletion2, match)
                else:
                    d[i, j, z] = min(insertion, deletion, deletion2)
    return len(way(d, n, m, s))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

