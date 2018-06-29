#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

Given two n-element data sets, X and Y, calculate the value of the Spearman's rank correlation coefficient.
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


def pearson_rank_correlation_coefficient(X, Y):
    rank_x = rank(X)
    rank_y = rank(Y)
    return pearson_correlation_coefficient(rank_x, rank_y)


def rank(n):
    return [sorted(n).index(v)+1 for v in n]

def pearson_unique_rank_correlation_coefficient(X, Y):
    rank_x = rank(X)
    rank_y = rank(Y)
    d2 = [(rank_x[i] - rank_y[i]) ** 2 for i in range(len(X))]
    return 1 - (6 * sum(d2)) / (len(X) * (len(X) * len(X) - 1))

n = int(input())
X = list(map(float, input().rstrip().split()))
Y = list(map(float, input().rstrip().split()))

print(round(pearson_rank_correlation_coefficient(X, Y), 3))
