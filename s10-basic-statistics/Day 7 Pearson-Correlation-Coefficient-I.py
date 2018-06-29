#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.
"""


def mean(n):
    return sum(n) / len(n)


def stddev(n):
    mu = mean(n)
    return math.sqrt(sum([(x - mu) ** 2 for x in n]) / len(n))


def pearson_correlation_coefficient(X, Y):
    x_mean = mean(X)
    y_mean = mean(Y)
    return sum([(x - x_mean) * (y - y_mean) for x, y in zip(X, Y)]) / (len(X) * stddev(X) * stddev(Y))


n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

print(round(pearson_correlation_coefficient(X, Y), 3))
