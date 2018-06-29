#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

The number of tickets purchased by each student for the University X vs. University Y football game follows a 
distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
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
tickets = 250  # float(input())
studens = 100  # float(input())
mean = 2.4  # float(input())
standard_deviation = 2.0  # float(input())

print(round(cumulative_distribution(0, tickets, studens * mean, standard_deviation * math.sqrt(studens)), 4))
