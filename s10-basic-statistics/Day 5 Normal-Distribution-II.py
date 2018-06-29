#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

The final grades for a Physics exam taken by a large group of students have a mean of mu = 70 and a standard 
deviation of 10. If we can approximate the distribution of these grades by a normal distribution, what percentage 
of the students:

1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?
"""


def normal_distribution(x, mean, standard_deviation):
    """
    :param x:
    :param mean:
    :param standard_deviation:
    :return:
    """
    return math.exp(-math.pow(x - mean, 2) / (2 * math.pow(standard_deviation, 2))) / (
            standard_deviation * math.sqrt(2 * math.pi))


def cumulative_distribution(lower, upper, mean, standard_deviation):
    lower = 0.5 * (1 + math.erf((lower - mean) / (standard_deviation * math.sqrt(2))))
    upper = 0.5 * (1 + math.erf((upper - mean) / (standard_deviation * math.sqrt(2))))
    return upper - lower


# Inputs
mean, standard_deviation = list(map(float, input().rstrip().split()))  # [70, 10]
grade_1 = float(input())  # 80
passing_grade = float(input())  # 60

# 1. Scored higher than 80 (i.e., have a grade > 80)?
print(round(100 * cumulative_distribution(grade_1, math.inf, mean, standard_deviation), 2))

# 2. Passed the test (i.e., have a grade >= 60)?
print(round(100 * cumulative_distribution(passing_grade, math.inf, mean, standard_deviation), 2))

# 3. Failed the test (i.e., have a grade < 60)?
print(round(100 * cumulative_distribution(0, passing_grade, mean, standard_deviation), 2))
