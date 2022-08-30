# python3



def compute_min_number_of_refills_rec(current_loc, d, m, stops):
    if current_loc + m >= d:
        return 0
    if not stops or (stops[0] - current_loc > m):
        return -1
    last_stop = current_loc
    while stops and (stops[0] - current_loc <= m):
        last_stop = stops[0]
        stops.pop(0)

    res = compute_min_number_of_refills_rec(last_stop, d, m, stops)
    if res == -1:
        return -1
    return 1 + res

def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    return compute_min_number_of_refills_rec(0, d, m, stops)


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
