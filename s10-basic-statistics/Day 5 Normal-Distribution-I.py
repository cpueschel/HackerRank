#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean 
of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

Less than 19.5 hours?
Between 20 and 22 hours?
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
mean, standard_deviation = list(map(float, input().rstrip().split()))  # [20, 2]
q1_hours = float(input())  # 19.5
q2_lower, q2_upper = list(map(float, input().rstrip().split()))  # [20, 22]

# Q1. Less than 19.5 hours?
print(round(cumulative_distribution(0, q1_hours, mean, standard_deviation), 3))

# Q2. Between 20 and 22 hours?
print(round(cumulative_distribution(q2_lower, q2_upper, mean, standard_deviation), 3))
