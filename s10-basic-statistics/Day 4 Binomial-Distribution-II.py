#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they 
are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?

1. P( R <= 2, n, p) = Sum from r=0 to 2( b( x= r, n, p) )
2. P( R >= 2, n, p) = Sum from r=2 to 10( b( x= r, n, p) )
"""


def combination(x, n):
    """
    :param x: unordered arrangement of x objects
    :param n: number of possible objects
    :return:
    """
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def binomial_distribution(x, n, p):
    """

    :param x: number of successes
    :param n: number of trials
    :param p: probability of sucess of 1 trial is p
    q = 1 - p (ie. failure of p)
    """
    q = 1 - p
    return combination(x, n) * math.pow(p, x) * math.pow(q, n - x)


def cumulative_distribution(values, n, p):
    return round(sum([binomial_distribution(x, n, p) for x in values]), 3)


percentage_rejected, N = input().split(" ")  # 12, 10#
percentage_rejected, N = int(percentage_rejected), int(N)
p_reject = percentage_rejected / 100

# 1. No more than 2 rejects?
print(cumulative_distribution(range(0, 3), N, p_reject))

# 2. At least 2 rejects?
print(cumulative_distribution(range(2, N + 1), N, p_reject))
