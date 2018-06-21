#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sums = []
    for row in range(0, len(arr) - 2):
        for col in range(0, len(arr[0]) - 2):
            a = arr[row][col]
            b = arr[row][col + 1]
            c = arr[row][col + 2]
            d = arr[row + 1][col + 1]
            e = arr[row + 2][col]
            f = arr[row + 2][col + 1]
            g = arr[row + 2][col + 2]
            hourglass_sums.append(sum([a, b, c, d, e, f, g]))

    return max(hourglass_sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
