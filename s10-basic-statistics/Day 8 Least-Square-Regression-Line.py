#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list 
of (x,y) points:
95 85
85 95
80 70
70 65
60 70

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? 
Determine the equation of the best-fit line using the least squares method, then compute and print the value of y 
when x=80.

Regression Line
Yhat = a + bX
"""


def mean(n):
    return sum(n) / len(n)


def stddev(n):
    mu = mean(n)
    return math.sqrt(sum([(x - mu) ** 2 for x in n]) / len(n))


def pearson_correlation_coefficient(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
    return sum([(x - x_mean) * (y - y_mean) for x, y in zip(x, y)]) / (len(x) * stddev(x) * stddev(y))


def b(x, y):
    """
    pearson correlation coeffient * std-dev_y/ std-dev_x
    :param x:
    :param y:
    :return:
    """
    return pearson_correlation_coefficient(x, y) * stddev(y) / stddev(x)


def a(x, y, b_value):
    return mean(y) - b_value * mean(x)

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

b_value = b(X, Y)
a_value = a(X, Y, b_value)

print(round(a_value + b_value * 80, 3))