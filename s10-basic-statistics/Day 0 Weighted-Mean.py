#!/bin/python3

import math
import os
import random
import re
import sys


def weighted_mean(array, weights):
    return sum(i[0] * i[1] for i in zip(array, weights)) / sum(weights)


if __name__ == '__main__':
    """
    Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, 
    calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of  
    decimal place (i.e.,  format).
    
    The first line contains an integer, N, denoting the number of elements in arrays X and W. 
    The second line contains N space-separated integers describing the respective elements of array X. 
    The third line contains N space-separated integers describing the respective elements of array W.
    """

    N = int(input())
    X = list(map(int, input().rstrip().split()))
    W = list(map(int, input().rstrip().split()))
    # n = 5
    # X = [10, 40, 30, 50, 20]
    # W = [1, 2, 3, 4, 5]
    print(round(weighted_mean(X, W), 1))
