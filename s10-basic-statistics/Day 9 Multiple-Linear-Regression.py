#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np

"""
Task:

Fit multiple values to linear regressions and then use them to find Y values
"""


class LinearRegression(object):
    def __init__(self):
        self.constants = None
        self.number_features = None
        self.B = None

    def train(self, dtrain, y):
        """
        Y = X * B
        X_T * Y = X_T * X * B
        INVERSE(X_T * X) * X_T * Y = I * B
        B = INVERSE(X_T * X) * X_T * Y
        """
        self.number_features = len(dtrain[0])

        X = []
        for row in dtrain:
            X.append([1] + row)

        X = np.array(X)
        Y = np.array(y)
        self.B = np.linalg.inv(X.T @ X) @ X.T @ Y

    def predict(self, dtest):
        return [np.array([1] + data) @ self.B for data in dtest]


# Inputs
# m is # of observed features
# n is # of feature sets
m, n = list(map(float, input().rstrip().split()))

dtrain = []
y = []
for i in range(0, int(n)):
    feature_set = list(map(float, input().rstrip().split()))
    dtrain.append(feature_set[:-1])
    y.append(feature_set[-1])

# number of feature sets
q = int(input())

dtest = []
for i in range(0, q):
    dtest.append(list(map(float, input().rstrip().split())))

linear = LinearRegression()
linear.train(dtrain, y)
for prediction in linear.predict(dtest):
    print(round(prediction, 2))
