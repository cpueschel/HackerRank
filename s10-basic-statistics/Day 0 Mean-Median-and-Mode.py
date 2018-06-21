#!/bin/python3

import math
import os
import random
import re
import sys


def calculateMean(n):
    return sum(n) / len(n)


def calculateMedian(n):
    n.sort()
    if len(n) % 2 != 0:
        return n[len(n) // 2]
    else:
        middle_element = n[len(n) // 2]
        middle_element += n[(len(n) // 2) - 1]
        return middle_element / 2


def calculateMode(n):
    mode_dict = {}
    for val in n:
        if val in mode_dict.keys():
            mode_dict[val] += 1
        else:
            mode_dict[val] = 1

    max_val = max(mode_dict, key=lambda k: mode_dict[k])
    mode = max_val
    for key, val in mode_dict.items():
        if mode_dict[mode] == val and key <= mode:
            mode = key
    return mode


if __name__ == '__main__':
    """
    The first line contains an integer, N , denoting the number of elements in the array. 
    The second line contains n space-separated integers describing the array's elements.
    """
    N = int(input())
    n = list(map(int, input().rstrip().split()))

    # N = 10
    # n = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
    print(calculateMean(n))
    print(calculateMedian(n))
    print(calculateMode(n))