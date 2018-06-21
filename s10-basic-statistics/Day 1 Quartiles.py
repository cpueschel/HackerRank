#!/bin/python3

import math
import os
import random
import re
import sys


def calculateMedian(n):
    n.sort()
    if len(n) % 2 != 0:
        return n[len(n) // 2]
    else:
        middle_element = n[len(n) // 2]
        middle_element += n[(len(n) // 2) - 1]
        return middle_element / 2


def first_quartile(n):
    n.sort()
    return int(calculateMedian(n[: (len(n) // 2)]))


def second_quartile(n):
    n.sort()
    return int(calculateMedian(n))


def third_quartile(n):
    n.sort()
    if len(n) % 2 != 0:
        return int(calculateMedian(n[(len(n) // 2) + 1:]))
    else:
        return int(calculateMedian(n[(len(n) // 2):]))


if __name__ == '__main__':
    """
    The first line contains an integer, n, denoting the number of elements in the array. 
    The second line contains n space-separated integers describing the array's elements.
    
    Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), 
    and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
    """
    #
    n = int(input())
    X = list(map(int, input().rstrip().split()))

    # n = 5
    # X = [10, 40, 30, 50, 20]

    print(first_quartile(X))
    print(second_quartile(X))
    print(third_quartile(X))
