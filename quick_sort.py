#!C:\Python27
# -*- coding: utf-8 -*-
import sys, os, datetime


def quick_sort1(a):
    if a == []:
        return a

    p = choose_pivot(a)

    left = []
    right = []

    for i in a:
        if i < p:
            left.append(i)
        else:
            right.append(i)

    left = quick_sort1(left)
    right = quick_sort1(right)

    return left + right


def choose_pivot(b):

    return b[0]


def quick_sort2(a):




    return a


def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort1(x [for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater







a = [3, 15, 4, 1, 7, 9, 2, 23, 20, 5]
b = [1,2]
c = [1]

print "choose_pivot"
print a
print choose_pivot(a), "\n"




a = [3, 15, 4, 1, 7, 9, 2, 23, 20]

print "quick_sort1"
print a
print qsort1(a), "\n"

