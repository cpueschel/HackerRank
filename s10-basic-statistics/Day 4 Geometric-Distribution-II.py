#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
The probability that a machine produces a defective product is 1/3. What is the probability 
that the 1st defect is found during the first 5 inspections?
"""


def negative_binomial_distribution(x, n, p):
    """

    :param x: number of successes
    :param n: number of trials
    :param p: probability of sucess of 1 trial is p
    q = 1 - p (ie. failure of p)
    """
    q = 1 - p
    return combination(x - 1, n - 1) * math.pow(p, x) * math.pow(q, n - x)


def cumulative_negative_binomial_distribution(x, values, p):
    return round(sum([negative_binomial_distribution(x, n, p) for n in values]), 3)


def combination(x, n):
    """
    :param x: unordered arrangement of x objects
    :param n: number of possible objects
    :return:
    """
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


inputs = list(map(int, input().rstrip().split()))  # [1,3]
p_defect = inputs[0] / inputs[1]
inspection_number = int(input())  # 5
print(round(cumulative_negative_binomial_distribution(1, range(1, inspection_number + 1), p_defect), 3))
