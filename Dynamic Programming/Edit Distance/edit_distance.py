# python3
import numpy as np


def edit_distance(first_string, second_string):
    n, m = len(first_string) + 1, len(second_string) + 1
    d = np.zeros((n, m))
    d[:, 0] = list(range(n))
    d[0, :] = list(range(m))
    for i in range(1, n):
        for j in range(1, m):
            insertion = d[i, j-1] + 1
            deletion = d[i-1, j] + 1
            match = d[i-1, j-1]
            mismatch = d[i-1, j-1] + 1
            if first_string[i-1] == second_string[j-1]:
                d[i, j] = min(insertion, deletion, match)
            else:
                d[i, j] = min(insertion, deletion, mismatch)
    return int(d[n-1, m-1])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
