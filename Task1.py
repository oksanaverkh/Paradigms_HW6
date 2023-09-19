# Бинарный поиск
# Ваша задача
# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

import random
from math import ceil


def binarySort(arr, num):
    center = len(arr) // 2
    left = 0
    right = len(arr) - 1

    while num != arr[center] and left <= right:
        if num > arr[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left+right)//2

    if left <= right:
        return center
    else:
        return -1


def main():
    array = []
    for i in range(random.randint(1, 10)):
        array.append(random.randint(-100, 100))
    array = sorted(array)
    print(array)
    number = int(input("\nEnter a number: "))
    print(f'\nIndex of the element in array: {binarySort(array, number)}')


if __name__ == "__main__":
    main()
