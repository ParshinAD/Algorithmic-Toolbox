# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    j = left
    k = 0
    for i in range(left+1, right+1):
        if x == array[i]:
            k += 1
            array[i], array[j+k] = array[j+k], array[i]
        if array[i] < x:
            j += 1
            array[j], array[j+k] = array[j+k], array[j]
            if j+k != i:
                array[i], array[j] = array[j], array[i]
    array[left], array[j] = array[j], array[left]
    return j, j+k


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    mid1, mid2 = partition3(array, left, right)
    randomized_quick_sort(array, left, mid1-1)
    randomized_quick_sort(array, mid2+1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
