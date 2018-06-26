#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:
A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random 
variable X is equal to 5.
"""


def poisson_distribution(k, lmbda):
    return math.pow(lmbda, k) * math.exp(- lmbda) / math.factorial(k)


mean = float(input())
X = int(input())
print(round(poisson_distribution(X, mean), 3))
