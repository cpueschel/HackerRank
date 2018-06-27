#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

"""


def expected_value(mean):
    return math.sqrt(mean + math.pow(mean, 2))


def machine_a(x):
    return 160 + 40 * math.pow(expected_value(x), 2)


def machine_b(x):
    return 128 + 40 * math.pow(expected_value(x), 2)


mean_a, mean_b = list(map(float, input().rstrip().split()))

# Cost of Machine A per day
print(round(machine_a(mean_a), 3))

# Cost of Machine B per day
print(round(machine_b(mean_b), 3))
