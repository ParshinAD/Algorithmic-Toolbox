from itertools import product
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


# i use here shortest solution, but maybe i can use any(?)
def shortest_sum(goal, values, used=[]):
    W = [50] * (goal + 1)
    W[0] = 0
    way = [[] for _ in range(goal+1)]
    for i in range(1, goal+1):
        for v in range(len(values)):
            val = values[v]
            if val <= i:
                new_val = W[i-val] + 1
                if new_val < W[i] and v not in way[i-val] + used:
                    W[i] = new_val
                    way[i] = way[i-val] + [v]
    return W[goal], way[goal]


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if sum(values) % 3:
        return 0
    split_sum = int(sum(values)/3)
    used = []
    for i in range(3):
        res, indexes = shortest_sum(split_sum, values, used)
        used += indexes
        if res == 50:
            return 0
    return 1



if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
