#!/bin/python3

import os


# Complete the reverseArray function below.
def reverseArray(a):
    reversed_array = []
    for i in range(0, len(a)):
        reversed_array.append(a[len(a) - 1 - i])
    return reversed_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
