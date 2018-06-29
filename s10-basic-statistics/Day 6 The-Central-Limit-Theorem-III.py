#!/bin/python3

import math
import os
import random
import re
import sys

"""
Task:

You have a sample of 100 values from a population with mean of 500 and with standard deviation 80. Compute the interval
that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that
P(A < x < B) = 0.95. Use the value of z=1.96. Note that z is the z-score.

"""

# Inputs
sample_size = 100  # float(input())
mean = 500  # float(input())
standard_deviation = 80  # float(input())
fraction = 0.95
z = 1.96

z_calc = z * standard_deviation / math.sqrt(sample_size)

# A
print(round(mean - z_calc, 2))
# B
print(round(mean + z_calc, 2))
