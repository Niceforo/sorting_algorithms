#!C:\Python27
# -*- coding: utf-8 -*-
import sys, os, datetime
import random


def selection_sort1(array):

    for i in range(0, len(array) - 1):

        MIN = array.index(min(array[i:]))
        array[i], array[MIN] = array[MIN], array[i]

    return array


def mi333n(array):
    """bla bla"""

    pass


def selection_sort2(array):

    for i in range(0, len(array) - 1):

        MIN = i
        for j in range(i + 1, len(array)):

            if array[j] < array[MIN]:
                MIN = j

        array[i], array[MIN] = array[MIN], array[i]

    return array


def selection_sort3(i, array):

    if i == len(array):
        return array

    MIN = i

    for j in range(i + 1, len(array)):
        if array[j] <= array[MIN]:
            MIN = j

    array[i], array[MIN] = array[MIN], array[i]

    selection_sort3(i + 1, array)

    return array


array = [3, 15, 4, 1, 7, 9, 4, 23, 20]
# array = []

print "selection_sort1"
print array
print selection_sort1(array), "\n"

array = [3, 15, 4, 1, 7, 9, 4, 23, 20]
# array = []

print "selection_sort2"
print array
print selection_sort2(array), "\n"

array = [3, 15, 4, 1, 7, 9, 4, 23, 20]
# array = []

print "selection_sort3"
print array
print selection_sort3(0, array), "\n"









