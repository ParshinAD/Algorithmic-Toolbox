# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def get_biggest(numbers):
    if not numbers:
        return -1
    numbers = list(map(str,numbers))
    max_lenght = len(max(numbers, key=len))
    numbers = sorted(numbers, key = lambda num: str(num * (max_lenght//len(num)+1)), reverse = True)
    return int(''.join(numbers))

def largest_number(numbers):
   return get_biggest(numbers)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
