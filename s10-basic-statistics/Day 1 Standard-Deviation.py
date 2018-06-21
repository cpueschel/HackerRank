#!/bin/python3

import math
import os
import random
import re
import sys


def mean(n):
    return sum(n) / len(n)


def calculateStdDev(n):
    mu = mean(n)
    return math.sqrt(sum([(x - mu) ** 2 for x in n]) / len(n))


if __name__ == '__main__':
    """
    Standard Deviation
    """
    #
    n = int(input())
    X = list(map(int, input().rstrip().split()))

    # X = [6, 12, 8, 10, 20, 16]
    print(round(calculateStdDev(X), 1))
