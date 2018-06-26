#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

"""


def poisson_distribution(k, lmbda):
    return math.pow(lmbda, k) * math.exp(- lmbda) / math.factorial(k)


def expected_value(mean):
    math.sqrt(mean + math.pow(mean, 2))


def machine_a(x):
    return 160 + 40 * math.pow(x, 2)


def machine_b(x):
    return 128 + 40 * math.pow(x, 2)


mean_a, mean_b = list(map(float, input().rstrip().split()))

# Cost of Machine A per day
a_chance = poisson_distribution(1, mean_a)
print(round(machine_a(a_chance), 3))

# Cost of Machine B per day
b_chance = poisson_distribution(1, mean_b)
print(round(machine_b(b_chance), 3))
