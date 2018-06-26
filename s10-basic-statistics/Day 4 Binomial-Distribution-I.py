#!/bin/python3

import math
import os
import random
import re
import sys

"""
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
P(B) = 1.09 / 2.09
P(G) = 1 / 2.09

P( B >= 3, n, p) = Sum from r=3 to 6( b( x= r, n, p) )
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


B, G = input().split(" ")  # 1.09, 1  #
p_b = B / (B + G)
print(cumulative_distribution(range(3, 7), 6, p_b))
