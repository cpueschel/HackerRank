#!/bin/python3

import os


# Complete the solve function below.
def solve(a, b):
    score_a, score_b = 0, 0
    for a_item, b_item in zip(a, b):
        if a_item > b_item:
            score_a += 1
        elif b_item > a_item:
            score_b += 1
    return score_a, score_b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
