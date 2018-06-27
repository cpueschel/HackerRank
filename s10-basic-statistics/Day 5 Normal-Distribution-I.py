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




# Inputs
mean, standard_deviation = list(map(float, input().rstrip().split()))