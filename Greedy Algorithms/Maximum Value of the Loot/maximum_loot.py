# python3

from sys import stdin


def maximum_loot_value_rec(capacity, weights, prices):
    if not prices or not capacity:
        return 0
    price_per_pound = list(map(lambda x, y: x/y, prices, weights))
    best_compounds_ind = price_per_pound.index(max(price_per_pound))
    value = price_per_pound[best_compounds_ind] * min(capacity, weights[best_compounds_ind])
    capacity = capacity - min(capacity, weights[best_compounds_ind])
    del weights[best_compounds_ind]
    del prices[best_compounds_ind]
    return value + maximum_loot_value_rec(capacity, weights, prices)


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    return maximum_loot_value_rec(capacity, weights, prices)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
