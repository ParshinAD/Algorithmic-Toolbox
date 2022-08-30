# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    res = []
    while segments:
        current_line = min(segments, key=lambda x: x.end - x.start)
        contain = max([(sum([x.start <= i and i <= x.end for x in segments]),
                        i,
                        [x for x in segments if x.start <= i and i <= x.end])\
                       for i in range(current_line.start, current_line.end+1)])
        res.append(contain[1])
        for segment in contain[2]:
            segments.remove(segment)
    return res


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
