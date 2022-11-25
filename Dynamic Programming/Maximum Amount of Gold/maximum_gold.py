# python3
import numpy as np

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    W = np.zeros((len(weights)+1, capacity+1))
    for w in range(1, len(weights) + 1):
        for i in range(1, capacity+1):
            W[w][i] = W[w-1][i]
            if weights[w-1] <= i:
                val = W[w-1][i-weights[w-1]] + weights[w-1]
                if val > W[w][i]:
                    W[w][i] = val
    return int(W[w][i])


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
