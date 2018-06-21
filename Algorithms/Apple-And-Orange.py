#!/bin/python3

import math
import os
import random
import re
import sys


def landedOnHouse(s,t,distance_from_tree,tree_location):
    location_fallen = tree_location + distance_from_tree
    return s <= location_fallen and location_fallen <= t

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    :param s: Starting point of Sam's house location.
    :param t: Ending location of Sam's house location.
    :param a: Location of the Apple tree.
    :param b: Location of the Orange tree.
    :param apples: distance each apple fell from the tree.
    :param oranges: distance each orange fell from the tree.
    :return:
    """
    apples_on_house = oranges_on_house = 0

    for apple in apples:
        apples_on_house += landedOnHouse(s, t, apple, a)

    for orange in oranges:
        oranges_on_house += landedOnHouse(s, t, orange, b)

    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
