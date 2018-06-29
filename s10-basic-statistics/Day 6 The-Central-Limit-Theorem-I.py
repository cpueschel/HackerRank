#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be 
transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds 
and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be 
safely loaded into the freight elevator and transported?
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
max_lbs = 9800  # float(input())
number_boxes = 49  # float(input())
mean = 205  # float(input())
standard_deviation = 15  # float(input())

print(round(cumulative_distribution(0, max_lbs, number_boxes * mean, standard_deviation * math.sqrt(number_boxes)), 4))
