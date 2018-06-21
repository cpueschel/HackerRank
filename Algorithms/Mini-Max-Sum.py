#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = sum(sorted(arr)[:4])
    max_sum = sum(sorted(arr, reverse=True)[:4])
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
