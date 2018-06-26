#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
The probability that a machine produces a defective product is 1/3. What is the probability 
that the 1st defect is found during the 5th inspection?
"""


def geometric_distribution(n, p):
    """
    :param n: number of independent trials
    :param p: probability of success
    :return:
    """
    q = 1 - p
    return math.pow(q, n - 1) * p


inputs = list(map(int, input().rstrip().split()))  # [1,3]
p_defect = inputs[0] / inputs[1]
inspection_number = int(input())  # 5
print(round(geometric_distribution(inspection_number, p_defect), 3))
