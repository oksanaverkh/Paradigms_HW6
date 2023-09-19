# Бинарный поиск
# Ваша задача
# Написать программу на любом языке в любой парадигме для бинарного поиска.
# На вход подаётся целочисленный массив и число.
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

import random


def centerFind(arr):
    if len(arr) % 2 == 0:
        return len(arr)//2-1
    else:
        return len(arr)//2


def numberFind(arr, num):
    count = 0
    for i in range(len(arr)):
        if arr[i] == num:
            count += 1
            break
    if count == 0:
        return -1
    else:
        return i


def binarySort(arr, num):
    center = centerFind(arr)
    if num > arr[center]:
        return numberFind(arr[center:], num) + center
    elif num == arr[center]:
        return center
    else:
        return numberFind(arr[:center], num)


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
