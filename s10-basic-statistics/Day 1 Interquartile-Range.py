#!/bin/python3

import math
import os
import random
import re
import sys


def calculateMedian(n):
    if len(n) % 2 != 0:
        return n[len(n) // 2]
    else:
        middle_element = n[len(n) // 2]
        middle_element += n[(len(n) // 2) - 1]
        return middle_element / 2


def first_quartile(n):
    return calculateMedian(n[: (len(n) // 2)])


def third_quartile(n):
    if len(n) % 2 != 0:
        return calculateMedian(n[(len(n) // 2) + 1:])
    else:
        return calculateMedian(n[(len(n) // 2):])


def calculate_interquartile_range(n):
    n.sort()
    q1 = first_quartile(n)
    q2 = third_quartile(n)
    return float(q2 - q1)


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
    F= list(map(int, input().rstrip().split()))
    # X = [6, 12, 8, 10, 20, 16]
    # F = [5, 6, 7, 8, 9, 10]

    Z = []
    for x, f in zip(X, F):
        Z += [x for each in range(0, f)]
    print(round(calculate_interquartile_range(Z), 1))
